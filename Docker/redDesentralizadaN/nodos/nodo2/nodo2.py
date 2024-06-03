from flask import Flask, jsonify, request, Response
import requests

app = Flask(__name__)

frase1 = "Alegria, hermoso destello de los dioses!"
frase2 = "frase2 en espera..."
frase3 = "frase3 en espera..."
frase4 = "frase4 en espera..."
frase5 = "frase5 en espera..."
frase6 = "frase6 en espera..."
frase7 = "frase7 en espera..."
frase8 = "frase8 en espera..."
id_frase1 = "2"

@app.route('/nodo2hacianodo6', methods=['GET'])
def ofrecer_frase_nodo2_a_nodo6():
    global frase1, frase2, frase3, frase4, frase5, frase6, frase7, frase8, id_frase4

    response_nodo5 = requests.get('http://192.168.1.15:5005/nodo5hacianodo2')

    if response_nodo5.status_code == 200:
        data_nodo5 = response_nodo5.json()
        for i in range(1, 9):
            frase = data_nodo5.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase4 = data_nodo5.get('id', '')
    else:
        return jsonify({'error': 'No se pudo obtener la frase del nodo 5'}), 500

    response_nodo0 = requests.get('http://192.168.1.10:5000/nodo0hacianodo2')

    if response_nodo0.status_code == 200:
        data_nodo0 = response_nodo0.json()
        for i in range(1, 9):
            frase = data_nodo0.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase4 = data_nodo0.get('id', '')
    else:
        return jsonify({'error': 'No se pudo obtener la frase del nodo 0'}), 500
    
    return jsonify({
        'frase1': frase1,
        'frase2': frase2,
        'frase3': frase3,
        'frase4': frase4,
        'frase5': frase5,
        'frase6': frase6,
        'frase7': frase7,
        'frase8': frase8,
        'id': id_frase1
    })

@app.route('/nodo2hacianodo0', methods=['GET'])
def ofrecer_frase_nodo2_a_nodo0():
    global frase1, frase2, frase3, frase4, frase5, frase6, frase7, frase8, id_frase1

    response_nodo5 = requests.get('http://192.168.1.15:5005/nodo5hacianodo2')

    if response_nodo5.status_code == 200:
        data_nodo5 = response_nodo5.json()
        for i in range(1, 9):
            frase = data_nodo5.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase1 = data_nodo5.get('id', '')
    else:
        return jsonify({'error': 'No se pudo obtener la frase del nodo 5'}), 500

    response_nodo6 = requests.get('http://192.168.1.16:5006/nodo6hacianodo2')

    if response_nodo6.status_code == 200:
        data_nodo6 = response_nodo6.json()
        for i in range(1, 9):
            frase = data_nodo6.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase1 = data_nodo6.get('id', '')
    else:
        return jsonify({'error': 'No se pudo obtener la frase del nodo 6'}), 500
    
    return jsonify({
        'frase1': frase1,
        'frase2': frase2,
        'frase3': frase3,
        'frase4': frase4,
        'frase5': frase5,
        'frase6': frase6,
        'frase7': frase7,
        'frase8': frase8,
        'id': id_frase1
    })

@app.route('/nodo2hacianodo5', methods=['GET'])
def ofrecer_frase_nodo2_a_nodo5():
    global frase1, frase2, frase3, frase4, frase5, frase6, frase7, frase8, id_frase1

    response_nodo0 = requests.get('http://192.168.1.10:5000/nodo0hacianodo2')

    if response_nodo0.status_code == 200:
        data_nodo0 = response_nodo0.json()
        for i in range(1, 9):
            frase = data_nodo0.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase1 = data_nodo0.get('id', '')
    else:
        return jsonify({'error': 'No se pudo obtener la frase del nodo 0'}), 500

    response_nodo6 = requests.get('http://192.168.1.15:5006/nodo6hacianodo2')

    if response_nodo6.status_code == 200:
        data_nodo6 = response_nodo6.json()
        for i in range(1, 9):
            frase = data_nodo6.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase1 = data_nodo6.get('id', '')
    else:
        return jsonify({'error': 'No se pudo obtener la frase del nodo 6'}), 500
    
    return jsonify({
        'frase1': frase1,
        'frase2': frase2,
        'frase3': frase3,
        'frase4': frase4,
        'frase5': frase5,
        'frase6': frase6,
        'frase7': frase7,
        'frase8': frase8,
        'id': id_frase1
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
    app.run(host='0.0.0.0', port=5002)
