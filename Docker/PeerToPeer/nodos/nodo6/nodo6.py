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

@app.route('/obtener_numeros_vecino', methods=['GET'])
def obtener_numeros_vecino():

    nodo = request.args.get('nodo')
    if nodo not in nodos_vecinos:
        return jsonify({"error": "Nodo vecino no válido"}), 400

    try:
        response = requests.get(nodos_vecinos[nodo] + "/ofrecer_numeros_nodo" + nodo[-1])
        if response.status_code == 200:
            datos_nodo_vecino = response.json()
            sumatoria_actual_del_nodo_vecino = datos_nodo_vecino.get("sumatoria_actual_del_nodo" + nodo[-1], 0)
            
            global sumatoria_actual_del_nodo6
            sumatoria_actual_del_nodo6 += sumatoria_actual_del_nodo_vecino

            return jsonify({
                "mensaje": "Sumatoria actualizada con éxito",
                "sumatoria_actual_del_nodo6": sumatoria_actual_del_nodo6
            }), 200
        else:
            return jsonify({"error": "No se pudo obtener la sumatoria del nodo vecino"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)

