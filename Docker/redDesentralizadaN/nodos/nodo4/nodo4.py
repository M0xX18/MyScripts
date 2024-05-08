from flask import Flask, jsonify, request, Response
import requests

app = Flask(__name__)

frase1 = "frase1 en espera..."
frase2 = "frase2 en espera..."
frase3 = "frase3 en espera..."
frase4 = "frase4 en espera..."
frase5 = "frase5 en espera..."
frase6 = "frase6 en espera..."
frase7 = "todos los hombres vuelven a ser hermanos"
frase8 = "frase8 en espera..."
id_frase7 = "4"

@app.route('/nodo4hacianodo1', methods=['GET'])
def ofrecer_frase_nodo4_a_nodo1():
    global frase1, frase2, frase3, frase4, frase5, frase6, frase7, frase8, id_frase7

    response = requests.get('http://192.168.1.17:5007/nodo7hacianodo4')
    if response.status_code == 200:
        data = response.json()
        for i in range(1, 9):
            frase = data.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase7 = data.get('id', '')

    else:
        return jsonify({'error': 'No se pudo obtener la frase del nodo 7'}), 500
    
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

@app.route('/nodo4hacianodo7', methods=['GET'])
def ofrecer_frase_nodo4_a_nodo7():
    global frase1, frase2, frase3, frase4, frase5, frase6, frase7, frase8, id_frase7

    response_nodo1 = requests.get('http://192.168.1.11:5001/nodo1hacianodo4')
    if response_nodo1.status_code == 200:
        data_nodo1 = response_nodo1.json()
        for i in range(1, 9):
            frase = data_nodo1.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase7 = data_nodo1.get('id', '')

    else:
        return jsonify({'error': 'No se pudo obtener la frase del nodo 1'}), 500
    
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
    app.run(host='0.0.0.0', port=5004)
