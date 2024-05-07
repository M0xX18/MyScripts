from flask import Flask, jsonify

app = Flask(__name__)

frase1 = "frase1 en espera..."
frase2 = "frase2 en espera..."
frase3 = "frase3 en espera..."
frase4 = "frase4 en espera..."
frase5 = "Tu hechizo une de nuevo"
frase6 = "frase6 en espera..."
frase7 = "frase7 en espera..."
frase8 = "frase8 en espera..."
id_frase7 = "4"

@app.route('/nodo3hacianodo1', methods=['GET'])
def ofrecer_frases_nodo3_a_nodo1():
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
    app.run(host='0.0.0.0', port=5003)
