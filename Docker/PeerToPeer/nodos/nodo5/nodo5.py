from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

nodos_vecinos = {
    "nodo3": "http://172.18.0.13:5003",
    "nodo6": "http://172.18.0.16:5006"
}

numero_nodo5 = 5
sumatoria_actual_del_nodo5 = 5

@app.route('/ofrecer_numeros_nodo5', methods=['GET'])
def ofrecer_numeros_nodo5():
    return jsonify({
        "numero_nodo5": numero_nodo5,
        "sumatoria_actual_del_nodo5": sumatoria_actual_del_nodo5
    }), 200

@app.route('/obtener_nodo<id>/sumar_su_numero', methods=['GET'])
def sumar_numero_vecino(id):
    nodo = f"nodo{id}"
    try:
        response = requests.get(nodos_vecinos[nodo] + f"/ofrecer_numeros_{nodo}")
        if response.status_code == 200:
            datos_nodo = response.json()
            numero_nodo = datos_nodo.get(f"numero_{nodo}", 0)
            global sumatoria_actual_del_nodo5
            sumatoria_actual_del_nodo5 += numero_nodo
            return jsonify({
                "mensaje": f"Numero del {nodo} sumado exitosamente",
                "sumatoria_actual_del_nodo5": sumatoria_actual_del_nodo5
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
            global sumatoria_actual_del_nodo5
            sumatoria_actual_del_nodo5 += sumatoria_actual_del_nodo
            return jsonify({
                f"sumatoria_actual_del_{nodo}": sumatoria_actual_del_nodo,
                "sumatoria_actual_del_nodo5": sumatoria_actual_del_nodo5
            }), 200
        else:
            return jsonify({"error": f"No se pudo obtener la sumatoria del {nodo}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)

