from flask import Flask, jsonify

app = Flask(__name__)

frase1 = "frase1 en espera..."
frase2 = "frase2 en espera..."
frase3 = "Ebrios de entusiasmo entramos"
frase4 = "frase4 en espera..."
frase5 = "frase5 en espera..."
frase6 = "frase6 en espera..."
frase7 = "frase7 en espera..."
frase8 = "frase8 en espera..."
id_frase3 = "5"

@app.route('/nodo5hacianodo2', methods=['GET'])
def ofrecer_frases_nodo5_a_nodo2():
    return jsonify({
        'frase1': frase1,
        'frase2': frase2,
        'frase3': frase3,
        'frase4': frase4,
        'frase5': frase5,
        'frase6': frase6,
        'frase7': frase7,
        'frase8': frase8,
        'id': id_frase3
    })

@app.route('/nodo5', methods=['GET'])
def nodo5Fin():
    global frase1, frase2, frase3, frase4, frase5, frase6, frase7, frase8, id_frase3

    response_nodo2 = requests.get('http://192.168.1.12:5002/nodo2hacianodo5')

    if response_nodo2.status_code == 200:
        data_nodo2 = response_nodo2.json()
        for i in range(1, 9):
            frase = data_nodo2.get(f'frase{i}', '')
            if frase != f'frase{i} en espera...':
                globals()[f'frase{i}'] = frase
        id_frase3 = data_nodo2.get('id', '')
    else:
        return jsonify({'error': 'No se pudo obtener la frase del nodo 2'}), 500
    
    return jsonify({
        'frase1': frase1,
        'frase2': frase2,
        'frase3': frase3,
        'frase4': frase4,
        'frase5': frase5,
        'frase6': frase6,
        'frase7': frase7,
        'frase8': frase8,
        'id': id_frase3
    })

@app.route('/frase_completa', methods=['GET'])
def obtener_frase_completa():
    frase_completa = ' '.join([
        frase1, frase2, frase3,
        frase4, frase5, frase6,
        frase7, frase8
    ])
    return jsonify({'frase_completa': frase_completa})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
