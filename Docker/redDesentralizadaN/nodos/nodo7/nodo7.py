from flask import Flask, jsonify

app = Flask(__name__)

frase1 = "frase1 en espera..."
frase2 = "frase2 en espera..."
frase3 = "frase3 en espera..."
frase4 = "frase4 en espera..."
frase5 = "frase5 en espera..."
frase6 = "lo que la acerba costumbre había separado;"
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
