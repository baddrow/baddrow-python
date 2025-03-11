from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/lista', methods=['GET'])
def getLista():
    
    lista = ['A', 'B', 'C', 'D', 'E']   
    return jsonify(lista), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
