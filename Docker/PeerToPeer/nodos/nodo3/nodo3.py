from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

nodos_vecinos = {
    "nodo2": "http://172.18.0.12:5002",
    "nodo5": "http://172.18.0.15:5005"
}

numero_nodo3 = 3
sumatoria_actual_del_nodo3 = 3

@app.route('/ofrecer_numeros_nodo3', methods=['GET'])
def ofrecer_numeros_nodo3():
    return jsonify({
        "numero_nodo3": numero_nodo3,
        "sumatoria_actual_del_nodo3": sumatoria_actual_del_nodo3
    }), 200

@app.route('/obtener_numeros_vecinos', methods=['GET'])
def obtener_numeros_vecinos():

    sumatoria_total_vecinos = 0

    for nodo, url in nodos_vecinos.items():
        try:
            response = requests.get(url + "/ofrecer_numeros_" + nodo)
            if response.status_code == 200:
                datos_nodo_vecino = response.json()
                sumatoria_actual_del_nodo_vecino = datos_nodo_vecino.get("sumatoria_actual_del_" + nodo, 0)
                sumatoria_total_vecinos += sumatoria_actual_del_nodo_vecino
            else:
                return jsonify({"error": f"No se pudo obtener la sumatoria del {nodo}"}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    global sumatoria_actual_del_nodo3
    sumatoria_actual_del_nodo3 += sumatoria_total_vecinos

    return jsonify({
        "mensaje": "Sumatoria actualizada con éxito",
        "sumatoria_actual_del_nodo3": sumatoria_actual_del_nodo3
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

