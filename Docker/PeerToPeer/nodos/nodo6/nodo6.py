from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

nodos_vecinos = {
    "nodo5": "http://172.18.0.15:5005",
    "nodo4": "http://172.18.0.14:5004",
    "nodo7": "http://172.18.0.17:5007"
}

numero_nodo6 = 6
sumatoria_actual_del_nodo6 = 6

@app.route('/ofrecer_numeros_nodo6', methods=['GET'])
def ofrecer_numeros_nodo6():
    return jsonify({
        "numero_nodo6": numero_nodo6,
        "sumatoria_actual_del_nodo6": sumatoria_actual_del_nodo6
    }), 200

@app.route('/obtener_nodo<id>/sumar_su_numero', methods=['GET'])
def sumar_numero_vecino(id):
    nodo = f"nodo{id}"
    try:
        response = requests.get(nodos_vecinos[nodo] + f"/ofrecer_numeros_{nodo}")
        if response.status_code == 200:
            datos_nodo = response.json()
            numero_nodo = datos_nodo.get(f"numero_{nodo}", 0)
            global sumatoria_actual_del_nodo6
            sumatoria_actual_del_nodo6 += numero_nodo
            return jsonify({
                "mensaje": f"Numero del {nodo} sumado exitosamente",
                "sumatoria_actual_del_nodo6": sumatoria_actual_del_nodo6
            }), 200
        else:
            return jsonify({"error": f"No se pudo obtener el numero del {nodo}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/obtener_nodo<id>/sumatoria_actual', methods=['GET'])
def obtener_sumatoria_vecino(id):
    nodo = f"nodo{id}"
    try:
        response = requests.get(nodos_vecinos[nodo] + f"/ofrecer_numeros_{nodo}")
        if response.status_code == 200:
            datos_nodo = response.json()
            sumatoria_actual_del_nodo = datos_nodo.get(f"sumatoria_actual_del_{nodo}", 0)
            global sumatoria_actual_del_nodo6
            sumatoria_actual_del_nodo6 += sumatoria_actual_del_nodo
            return jsonify({
                f"sumatoria_actual_del_{nodo}": sumatoria_actual_del_nodo,
                "sumatoria_actual_del_nodo6": sumatoria_actual_del_nodo6
            }), 200
        else:
            return jsonify({"error": f"No se pudo obtener la sumatoria del {nodo}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)

