from flask import Flask, jsonify, request, Response
import requests

app = Flask(__name__)

frase1 = "frase1 en espera..."
frase2 = "hija del Eliseo!"
frase3 = "frase3 en espera..."
frase4 = "frase4 en espera..."
frase5 = "frase5 en espera..."
frase6 = "frase6 en espera..."
frase7 = "frase7 en espera..."
frase8 = "frase8 en espera..."
id_frase2 = "0"

@app.route('/nodo0hacianodo2', methods=['GET'])
def ofrecer_frase_nodo0_a_nodo2():
    global frase1, frase2, frase3, frase4, frase5, frase6, frase7, frase8, id_frase2

    response_nodo1 = requests.get('http://192.168.0.11:5001/nodo1hacianodo0')

    if response_nodo1.status_code == 200:
        data_nodo1 = response_nodo1.json()
        for i in range(1, 9):
            frase = data_nodo1.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase2 = data_nodo1.get('id', '')
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
        'id': id_frase2
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
    app.run(host='0.0.0.0', port=5000)
