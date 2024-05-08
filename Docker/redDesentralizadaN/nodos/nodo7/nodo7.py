from flask import Flask, jsonify

app = Flask(__name__)

frase1 = "frase1 en espera..."
frase2 = "frase2 en espera..."
frase3 = "frase3 en espera..."
frase4 = "frase4 en espera..."
frase5 = "frase5 en espera..."
frase6 = "lo que la acerba costumbre habia separado;"
frase7 = "frase7 en espera..."
frase8 = "frase8 en espera..."
id_frase7 = "4"

@app.route('/nodo7hacianodo4', methods=['GET'])
def ofrecer_frases_nodo7_a_nodo4():
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

@app.route('/nodo7', methods=['GET'])
def nodo7Fin():
    global frase1, frase2, frase3, frase4, frase5, frase6, frase7, frase8, id_frase7

    response_nodo4 = requests.get('http://192.168.1.14:5004/nodo4hacianodo7')

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
    frase_completa = ' '.join([
        frase1, frase2, frase3,
        frase4, frase5, frase6,
        frase7, frase8
    ])
    return jsonify({'frase_completa': frase_completa})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
