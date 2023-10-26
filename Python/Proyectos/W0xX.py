# Importar los módulos necesarios
import sys
import qtpy.QtWidgets as QtWidgets
import qtpy.QtWebEngineWidgets as QtWebEngineWidgets
import qtpy.QtCore as QtCore
import requests
import stem.process
from stem.util import term

# Definir una función para imprimir el estado del circuito de Tor
def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))

# Iniciar el proceso de Tor con Stem y obtener el puerto del proxy SOCKS
with stem.process.launch_tor_with_config(
     config={
         'SocksPort': '7000',
         'ControlPort': '9051',  # Cambia el puerto de control a 9051 u otro disponible
     },
     init_msg_handler=print_bootstrap_lines,
 ) as tor_process:
     socks_port = tor_process.get_socks_listeners()[0].get_info('local-address').split(':')[1]

# Crear una clase para el navegador web con funcionalidad Tor
class WebBrowser(QtWidgets.QMainWindow):

    # Inicializar el navegador web
    def __init__(self):
        super().__init__()

        # Crear una barra de herramientas con un campo de texto y un botón
        self.toolbar = QtWidgets.QToolBar()
        self.addToolBar(self.toolbar)
        self.url_input = QtWidgets.QLineEdit()
        self.go_button = QtWidgets.QPushButton("Ir")
        self.toolbar.addWidget(self.url_input)
        self.toolbar.addWidget(self.go_button)

        # Conectar el botón con la función para cargar la url
        self.go_button.clicked.connect(self.load_url)

        # Crear una vista web para mostrar el contenido de la página web
        self.web_view = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.web_view)

        # Mostrar el navegador web
        self.show()

    # Definir la función para cargar la url con el proxy Tor
    def load_url(self):
        # Obtener la url del campo de texto
        url = self.url_input.text()

        # Añadir el prefijo http:// si no está presente
        if not url.startswith("http://"):
            url = "http://" + url

        # Crear una sesión de requests con el proxy SOCKS de Tor
        session = requests.session()
        session.proxies = {'http':  'socks5://127.0.0.1:' + socks_port,
                           'https': 'socks5://127.0.0.1:' + socks_port}

        # Hacer una petición GET a la url utilizando el proxy Tor
        response = session.get(url)

        # Cargar la url en la vista web
        self.web_view.setUrl(QtCore.QUrl(url))

# Crear una aplicación y una instancia del navegador web
app = QtWidgets.QApplication(sys.argv)
browser = WebBrowser()
sys.exit(app.exec_())

# Detener el proceso de Tor al salir de la aplicación
tor_process.kill()

