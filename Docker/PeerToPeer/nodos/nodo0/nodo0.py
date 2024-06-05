from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

nodos_vecinos = {
    "nodo1": "http://172.18.0.11:5001"
}

numero_nodo0 = 10
sumatoria_actual_del_nodo0 = 10

@app.route('/ofrecer_numeros_nodo0', methods=['GET'])
def ofrecer_numeros_nodo0():
    return jsonify({
        "numero_nodo0": numero_nodo0,
        "sumatoria_actual_del_nodo0": sumatoria_actual_del_nodo0
    }), 200

@app.route('/obtener_numeros_nodo1', methods=['GET'])
def obtener_numeros_nodo1():
    try:
        response = requests.get(nodos_vecinos["nodo1"] + "/ofrecer_numeros_nodo1")
        if response.status_code == 200:
            datos_nodo1 = response.json()
            sumatoria_actual_del_nodo1 = datos_nodo1.get("sumatoria_actual_del_nodo1", 0)
            
            global sumatoria_actual_del_nodo0
            sumatoria_actual_del_nodo0 += sumatoria_actual_del_nodo1

            return jsonify({
                "mensaje": "Sumatoria actualizada con éxito",
                "sumatoria_actual_del_nodo0": sumatoria_actual_del_nodo0
            }), 200
        else:
            return jsonify({"error": "No se pudo obtener la sumatoria del nodo1"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

