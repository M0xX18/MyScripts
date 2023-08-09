#!/bin/bash

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

#Texto
Negrita="\e[1m"
Subrayado="\e[4m"

function ctrl_c (){
  echo -e "\n\n ${yellowColour}<!>${endColour}${redColour} ...SALIENDO... ${endColour}${yellowColour}<!>${endColour} \n"
  exit 1
}

#Variables globales
url="https://htbmachines.github.io/bundle.js"

#ctrl_c
trap ctrl_c INT

function helpPanel (){
  echo -e "\n\t\t ${yellowColour}<?> Uso de la aplicacion <?> ${endColour}\n"
  echo -e "\t ${Negrita}${greenColour}-h${endColour}\t Utiliza este panel de ayuda..."
  echo -e "\t ${Negrita}${greenColour}-a${endColour}\t Actualizacion de archivos necesarios..."
  echo -e "\t ${Negrita}${greenColour}-m${endColour}\t Busqueda por nombre de maquina..."
  echo -e "\t ${Negrita}${greenColour}-i${endColour}\t Busqueda por IP de maquina..."
  echo -e "\t ${Negrita}${greenColour}-y${endColour}\t Obtener el link del video de la maquina resuelta"
  echo -e "\t ${Negrita}${greenColour}-d${endColour}\t Busqueda por dificultad de maquina..."
  echo -e "\t ${Negrita}${greenColour}-s${endColour}\t Busqueda por las skills de maquina..."
  echo -e "\t ${Negrita}${greenColour}-o${endColour}\t Busqueda por Sistema Operativo de maquina..."
}

function updateMachines ()
{
  tput civis
  if [ ! -f bundle.js ]; then
    echo -e "\n ${yellowColour}<#>${endColour} ${greenColour}Descargando los Archivos necesarios${endColour} ${yellowColour}<#>${endColour}"
    curl -s $url > bundle.js
    js-beautify bundle.js | sponge bundle.js
    echo -e "\n ${yellowColour}<#>${endColour} ${greenColour}Todos los archivos se actualizaron correctamente${endColour} ${yellowColour}<#>${endColour}\n"
    tput cnorm
  else
    echo -e "\n ${yellowColour}<#>${endColour}${greenColour}...Comprobando si hay actualizaciones disponibles...${endColour}${yellowColour}<#>${endColour}"
    curl -s $url > bundle_actualizado.js
    js-beautify bundle_actualizado.js | sponge bundle_actualizado.js
    BundleFile=$(md5sum bundle.js | awk '{print $1}')
    tmpBundleFile=$(md5sum bundle_actualizado.js | awk '{print $1}')
    if [ $BundleFile == $tmpBundleFile ]; then 
      echo -e "\n ${yellowColour}<#>${endColour} ${greenColour}Los archivos se encuentran en su ultima version${endColour} ${yellowColour}<#>${endColour}" 
      rm bundle_actualizado.js
    else
      echo -e "\n ${yellowColour}<#>${endColour} ${greenColour}Los archivos se han actualizado correctamente${endColour} ${yellowColour}<#>${endColour}"
      rm bundle.js && mv bundle_actualizado.js bundle.js
    fi
  fi
  tput cnorm
}

function searchMachine (){
  machineChecker="$(cat bundle.js | awk "/name: \"${machineName}\"/,/resuelta:/" | grep -vE 'id:|sku:|resuelta:' | tr -d '"' | tr -d ',' | sed 's/^ *//')"
  
  if [ "$machineChecker" ]; then
    machineName="$1"
    echo -e "\n ${yellowColour}<#>${endColour} ${greenColour}...Verificando la informacion de la maquina... ${endColour}${blueColour}${machineName}${endColour} ${yellowColour}<#>${endColour}\n"
    sleep 1
    echo -e "${blueColour}${machineChecker}${endColour}\n"
  else
    echo -e "\n ${redColour}<!> La maquina ${yellowColour}$1${endColour}${redColour} no existe <!>${endColour}\n"
  fi 
}

function searchIP(){
  IPChecker="$(cat bundle.js | grep "ip: \"$IP\"" -B 3 | grep "name:" | awk '{print $2}' | tr -d '"' | tr -d ",")"

  if [ "$IPChecker" ]; then
    IP="$1"
    name="$(cat bundle.js | grep "ip: \"$IP\"" -B 3 | grep "name" | awk '{print $2}' | tr -d '"' | tr -d ",")"
    echo -e "\n ${yellowColour}<#>${endColour} ${greenColour}...La IP${endColour} ${turquoiseColour}${IP}${endColour} ${greenColour}corresponde a la maquina${endColour} ${blueColour}${name}${endColour}${greenColour}...${endColour} ${yellowColour}<#>${endColour}\n"
  else
    echo -e "\n ${redColour}<!> La maquina ${yellowColour}$1${endColour}${redColour} no existe <!>${endColour}\n" 
  fi
}

function getYoutube(){
  machineName="$1"
  link="$(cat bundle.js | awk "/name: \"Tentacle\"/,/resuelta:/" | grep -vE 'id:|sku:|resuelta:' | tr -d '"' | tr -d ',' | sed 's/^ *//' | grep "youtube" | awk 'NF{print $NF}')"
  if [ "$link" ]; then 
    echo -e "\n ${yellowColour}<#>${endColour}${greenColour} El video para la maquina ${blueColour}${machineName}${endColour} ${greenColour}esta en el siguiente enlace:${endColour} ${blueColour}${link}${endColour}${yellowColour} <#>${endColour}\n" 
  else
    echo -e "\n ${redColour}<!> La maquina ${yellowColour}$1${endColour}${redColour} no existe <!>${endColour}\n"
  fi
}

function getMachinesDificulty(){
  dificultad="$1"
  if [ $dificultad == "Facil" ]; then
    dificultad="Fácil"
  elif [ $dificultad == "Dificil" ]; then
    dificultad="Difícil"
  fi
  machinesFilter="$(cat bundle.js | grep "dificultad: \"$dificultad\"" -B 5 | grep "name:" | awk 'NF{print $NF}' | tr -d ',' | tr -d '"' | column)"
  if [ "$machinesFilter" ]; then
    echo -e "\n ${yellowColour}<#>${endColour}${greenColour} Las maquinas con Dificultad ${endColour}${redColour}$1 ${endColour}${greenColour}son las siguientes: ${endColour}${yellowColour}<#>${endColour}\n"
    echo -e "${blueColour}${machinesFilter}${endColour}"
  else
    echo -e "\n ${redColour}<!> La dificultad ${yellowColour}$1${endColour}${redColour} no existe, <!>${endColour}\n"
  fi
}

function getOS(){
  OS="$1"
  searchOS="$(cat bundle.js | grep "so: \"$1\"" -B 5 | grep "name: " | awk 'NF{print $NF}' | tr -d '"' | tr -d ',' | column)"
  if [ "$searchOS" ]; then 
    echo -e "\n ${yellowColour}<#>${endColour}${greenColour} Las maquinas con sistema operativo ${blueColour}${OS}${endColour}${greenColour} son las siguientes:${endColour}${yellowColour} <#>${endColour}\n"
    echo -e "${blueColour}${searchOS}${endColour}"
  else
    echo -e "\n ${redColour}<!> El sistema operativo ${yellowColour}${OS}${endColour}${redColour} no existe <!>${endColour}\n"
  fi
}

function getSkills(){
  Skills="$1"
  SkillsChecker="$(cat bundle.js | grep "skills: " -B 6 | grep "${Skills}" -i -B 6 | grep "name: " | awk 'NF{print $NF}' |tr -d '"' | tr -d "," | column)"
  if [ "$SkillsChecker" ]; then
    echo -e "\n ${yellowColour}<#>${endColour}${greenColour} Las maquinas que cuentan con la Skill de ${blueColour}${Skills}${endColour}${greenColour} son las siguientes:${endColour}${yellowColour} <#>${endColour}\n"
    echo -e "${blueColour}${SkillsChecker}${endColour}"
  else 
    echo -e "\n ${redColour}<!> No se ha encontrado una Skill cuyo nombre sea ${yellowColour}${Skills}${endColour}${redColour} <!>${endColour}\n" 
  fi
}

function getMaquinasPorOSyDificultad (){
  dificultad="$1"
  if [ $dificultad == "Facil" ]; then
    dificultad="Fácil"
  elif [ $dificultad == "Dificil" ]; then
    dificultad="Difícil"
  fi
  OS="$2"
  OSyDificultadChecker="$(cat bundle.js | grep "so: \"$OS\"" -C 4 | grep "dificultad: \"$dificultad\"" -B 5 | grep "name: " | awk 'NF{print $NF}' | tr -d '"' | tr -d ',' | column)"
  if [ "$OSyDificultadChecker" ]; then
    echo -e "\n ${yellowColour}<#>${endColour}${greenColour} Las maquinas con Dificultad ${endColour}${redColour}${dificultad}${endColour}${greenColour} y sistema operativo ${endColour}${blueColour}${OS}${endColour}${greenColour} son las siguientes:${endColour}${yellowColour} <#>${endColour}\n"
    echo -e "${blueColour}${OSyDificultadChecker}${endColour}"
  else
    echo -e "\n ${redColour}<!> La dificultad ${blueColour}${dificultad}${endColour}${redColour} o el sistema operativo ${endColour}${blueColour}${OS}${endColour}${redColour} no existe <!>${endColour}\n"
  fi
}

#Chivato
declare -i chivato_dificultad=0;
declare -i chivato_os=0;

#Indicadores
declare -i parameterCounter=0

while getopts "m:ai:y:d:o:s:h" arg; do
  case $arg in 
    m) machineName=$OPTARG; let parameterCounter+=1;;
    a) let parameterCounter+=2;;
    i) IP=$OPTARG; let parameterCounter+=3;;
    y) machineName=$OPTARG; let parameterCounter+=4;;
    d) dificultad=$OPTARG; chivato_dificultad=1; let parameterCounter+=5;;
    o) OS=$OPTARG; chivato_os=1; let parameterCounter+=6;;
    s) Skills=$OPTARG; let parameterCounter+=7;;
    h) ;;
  esac
done

if [ $parameterCounter -eq 1 ]; then
  searchMachine $machineName
elif [ $parameterCounter -eq 2 ]; then
  updateMachines
elif [ $parameterCounter -eq 3 ]; then
  searchIP $IP
elif [ $parameterCounter -eq 4 ]; then
  getYoutube $machineName
elif [ $parameterCounter -eq 5 ]; then
  getMachinesDificulty $dificultad
elif [ $parameterCounter -eq 6 ]; then
  getOS $OS
elif [ $parameterCounter -eq 7 ]; then
  getSkills "$Skills"
elif [ $chivato_dificultad -eq 1 ] && [ $chivato_os -eq 1 ]; then
  getMaquinasPorOSyDificultad $dificultad $OS
else
  helpPanel
fi
