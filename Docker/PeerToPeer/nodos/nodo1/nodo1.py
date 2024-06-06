from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

nodos_vecinos = {
    "nodo0": "http://172.18.0.10:5000",
    "nodo4": "http://172.18.0.14:5004",
    "nodo2": "http://172.18.0.12:5002"
}

numero_nodo1 = 6
sumatoria_actual_del_nodo1 = 6 

@app.route('/ofrecer_numeros_nodo1', methods=['GET'])
def ofrecer_numeros_nodo1():
    return jsonify({
        "numero_nodo1": numero_nodo1,
        "sumatoria_actual_del_nodo1": sumatoria_actual_del_nodo1
    }), 200

@app.route('/obtener_nodo<id>/sumar_su_numero', methods=['GET'])
def sumar_numero_vecino(id):
    nodo = f"nodo{id}"
    if nodo not in nodos_vecinos:
        return jsonify({"error": "Nodo vecino no válido"}), 400

    try:
        response = requests.get(nodos_vecinos[nodo] + f"/ofrecer_numeros_{nodo}")
        if response.status_code == 200:
            datos_nodo = response.json()
            numero_nodo = datos_nodo.get(f"numero_{nodo}", 0)
            global sumatoria_actual_del_nodo1
            sumatoria_actual_del_nodo1 += numero_nodo
            return jsonify({
                "mensaje": f"Número del {nodo} sumado exitosamente",
                "sumatoria_actual_del_nodo1": sumatoria_actual_del_nodo1
            }), 200
        else:
            return jsonify({"error": f"No se pudo obtener el número del {nodo}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/obtener_nodo<id>/sumatoria_actual', methods=['GET'])
def obtener_sumatoria_vecino(id):
    nodo = f"nodo{id}"
    if nodo not in nodos_vecinos:
        return jsonify({"error": "Nodo vecino no válido"}), 400

    try:
        response = requests.get(nodos_vecinos[nodo] + f"/ofrecer_numeros_{nodo}")
        if response.status_code == 200:
            datos_nodo = response.json()
            sumatoria_actual_del_nodo = datos_nodo.get(f"sumatoria_actual_del_{nodo}", 0)
            global sumatoria_actual_del_nodo1
            sumatoria_actual_del_nodo1 += sumatoria_actual_del_nodo
            return jsonify({
                f"sumatoria_actual_del_{nodo}": sumatoria_actual_del_nodo,
                "sumatoria_actual_del_nodo1": sumatoria_actual_del_nodo1
            }), 200
        else:
            return jsonify({"error": f"No se pudo obtener la sumatoria del {nodo}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

