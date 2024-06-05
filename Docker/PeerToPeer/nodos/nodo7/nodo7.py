from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

nodos_vecinos = {
    "nodo6": "http://172.18.0.10:5000"
}

numero_nodo7 = 10
sumatoria_actual_del_nodo7 = 10

@app.route('/ofrecer_numeros_nodo7', methods=['GET'])
def ofrecer_numeros_nodo7():
    return jsonify({
        "numero_nodo7": numero_nodo7,
        "sumatoria_actual_del_nodo7": sumatoria_actual_del_nodo7
    }), 200

@app.route('/obtener_numeros_nodo6', methods=['GET'])
def obtener_numeros_nodo6():

    try:
        response = requests.get(nodos_vecinos["nodo6"] + "/ofrecer_numeros_nodo6")
        if response.status_code == 200:
            datos_nodo6 = response.json()
            sumatoria_actual_del_nodo6 = datos_nodo6.get("sumatoria_actual_del_nodo6", 0)
            
            global sumatoria_actual_del_nodo7
            sumatoria_actual_del_nodo7 += sumatoria_actual_del_nodo6

            return jsonify({
                "mensaje": "Sumatoria actualizada con éxito",
                "sumatoria_actual_del_nodo7": sumatoria_actual_del_nodo7
            }), 200
        else:
            return jsonify({"error": "No se pudo obtener la sumatoria del nodo6"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)

