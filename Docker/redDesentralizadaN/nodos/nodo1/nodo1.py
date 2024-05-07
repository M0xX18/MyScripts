from flask import Flask, jsonify, request, Response
import requests

app = Flask(__name__)

frase1 = "frase1 en espera..."
frase2 = "frase2 en espera..."
frase3 = "frase3 en espera..."
frase4 = "diosa celestial, en tu santuario"
frase5 = "frase5 en espera..."
frase6 = "frase6 en espera..."
frase7 = "frase7 en espera..."
frase8 = "frase8 en espera..."
id_frase4 = "1"

@app.route('/nodo1hacianodo0', methods=['GET'])
def ofrecer_frase_nodo1_a_nodo0():
    global frase1, frase2, frase3, frase4, frase5, frase6, frase7, frase8, id_frase7

    response_nodo3 = requests.get('http://192.168.0.13:5003/nodo3hacianodo1')

    if response_nodo3.status_code == 200:
        data_nodo3 = response_nodo3.json()
        for i in range(1, 9):
            frase = data_nodo3.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase7 = data_nodo3.get('id', '')
    else:
        return jsonify({'error': 'No se pudo obtener la frase del nodo 3'}), 500

    response_nodo4 = requests.get('http://192.168.0.14:5004/nodo4hacianodo1')

    if response_nodo4.status_code == 200:
        data_nodo4 = response_nodo4.json()
        for i in range(1, 9):
            frase = data_nodo4.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase7 = data_nodo4.get('id', '')
    else:
        return jsonify({'error': 'No se pudo obtener la frase del nodo 4'}), 500
    
    return jsonify({
        'frase1': frase1,
        'frase2': frase2,
        'frase3': frase3,
        'frase4': frase4,
        'frase5': frase5,
        'frase6': frase6,
        'frase7': frase7,
        'frase8': frase8,
        'id': id_frase7
    })

@app.route('/frase_completa', methods=['GET'])
def obtener_frase_completa():
    frase_completa = (
        frase1 + " " + frase2 + " " + frase3 + " " +
        frase4 + " " + frase5 + " " + frase6 + " " +
        frase7 + " " + frase8
    )
    return jsonify({'frase_completa': frase_completa})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
