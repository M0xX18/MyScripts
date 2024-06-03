import hashlib
import time
import json
from uuid import uuid4
from flask import Flask, request, jsonify

app = Flask(__name__)

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.wallets = {}
        self.opener_closer = OpenCloser(self)

        self.wallets[self.hash('')] = 0

        self.crearBloque(proof=1, previous_hash='0', nonce=0)

    def registrarTx(self, sender, recipient, amount):
        sender_wallet = self.wallets.get(sender, None)
        recipient_wallet = self.wallets.get(recipient, None)

        if sender_wallet is None:
            return 'La wallet del remitente no existe', 400
        if recipient_wallet is None:
            return 'La wallet del destinatario no existe', 400
        if int(sender_wallet) < int(amount):
            return 'Saldo insuficiente en la wallet del remitente', 400

        self.wallets[sender] = int(sender_wallet) - int(amount)
        self.wallets[recipient] = int(recipient_wallet) + int(amount)

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': int(amount)
        })

        result = self.last_block['index'] + 1

        if len(self.current_transactions) % 3 == 0:
            # Calcular el nonce
            proof = self.proof_of_work(self.last_block['proof'])
            previous_hash = self.hash(self.last_block)
            nonce = self.calcular_nonce(proof, previous_hash)
            self.opener_closer.cerrarBloque(self.last_block, nonce)

        return result
    
    def crearBloque(self, proof, previous_hash, nonce):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,  # Agregado: incluir las transacciones en el bloque
            'proof': proof,
            'previous_hash': previous_hash,
            'nonce': nonce
        }
        self.chain.append(block)
        
        return block

    def calcular_nonce(self, proof, previous_hash):
        nonce = 0
        while not self.valid_nonce(proof, previous_hash, nonce):
            nonce += 1
        return nonce

    def valid_nonce(self, proof, previous_hash, nonce):
        guess = f'{proof}{previous_hash}{nonce}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @staticmethod
    def hash(block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

class OpenCloser:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def cerrarBloque(self, bloque, nonce):
        if len(bloque['transactions']) >= 3:
            proof = self.blockchain.proof_of_work(self.blockchain.last_block['proof'])
            previous_hash = self.blockchain.hash(self.blockchain.last_block)
            self.blockchain.crearBloque(proof, previous_hash, nonce)
            self.blockchain.current_transactions = []

class Validator:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def validar_transaccion(self, sender, recipient, amount):
        if sender not in self.blockchain.wallets:
            return 'La wallet del remitente no existe', 400
        if recipient not in self.blockchain.wallets:
            return 'La wallet del destinatario no existe', 400
        if self.blockchain.wallets[sender] < amount:
            return 'Saldo insuficiente en la wallet del remitente', 400
        return None

class Coordinator:
    def __init__(self):
        self.blockchain = Blockchain()
        self.validator = Validator(self.blockchain)

    def consultar_saldo(self, wallet):
        wallet_balance = self.blockchain.wallets.get(wallet, None)
        if wallet_balance is None:
            return 'La wallet no existe', 404
        saldo = wallet_balance
        return {'saldo': saldo}

    def crear_wallet(self):
        # Generar un hash SHA-256 único para la wallet (es unico por que se usa el uuid4 para su asignacion)
        wallet_hash = self.blockchain.hash(str(uuid4()))
        self.blockchain.wallets[wallet_hash] = 0
        return wallet_hash

    def registrar_transaccion(self, sender, recipient, amount):
        # Validar la transacción
        validation_error = self.validator.validar_transaccion(sender, recipient, amount)
        if validation_error:
            return validation_error

        # Registrar la transacción en el Blockchain
        index = self.blockchain.registrarTx(sender, recipient, amount)
        return index

    def obtener_chain(self):
        # Obtener la cadena completa de bloques
        return self.blockchain.chain

node_identifier = str(uuid4()).replace('-', '')

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Faltan valores', 400

    sender = values['sender']
    recipient = values['recipient']
    amount = values['amount']

    # Registrar la transacción
    response = coordinator.registrar_transaccion(sender, recipient, amount)
    if isinstance(response, int):
        return jsonify({'message': f'La transaccion sera agregada al bloque {response}'}), 201
    else:
        return response

@app.route('/wallet/saldo', methods=['GET'])
def consultar_saldo():
    wallet_hash = request.args.get('wallet')
    if wallet_hash is None:
        return 'Falta el parámetro "wallet"', 400
    response = coordinator.consultar_saldo(wallet_hash)
    return jsonify(response), 200

@app.route('/wallet/nueva', methods=['POST'])
def crear_wallet():
    # Generar una nueva wallet y devolver el hash
    wallet_hash = coordinator.crear_wallet()
    return jsonify({'message': f'Wallet generada con hash: {wallet_hash}'}), 201

@app.route('/chain', methods=['GET'])
def obtener_chain():
    # Obtener todos los bloques en el blockchain
    chain = coordinator.obtener_chain()
    response = {
        'chain': chain,
        'length': len(chain)
    }
    return jsonify(response), 200

@app.route('/wallet/recargar', methods=['POST'])
def recargar_wallet():
    try:
        data = request.get_json()
        required_fields = ['wallet', 'amount']

        if not all(field in data for field in required_fields):
            return 'Faltan campos obligatorios', 400

        wallet_hash = data['wallet']
        amount = data['amount']

        if wallet_hash not in coordinator.blockchain.wallets:
            return 'La wallet no existe', 400

        coordinator.blockchain.wallets[wallet_hash] = int(coordinator.blockchain.wallets[wallet_hash]) + int(amount)

        response_message = f'Se han recargado {amount} a la wallet con hash: {wallet_hash}'
        return jsonify({'message': response_message}), 201
    except Exception as e:
        print(f"Error en recargar_wallet: {str(e)}")
        return 'Error interno del servidor', 500


if __name__ == '__main__':
    coordinator = Coordinator()
    app.run(host='0.0.0.0', port=5000)
