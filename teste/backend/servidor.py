from config import *
from modelo import Trem

@app.route("/")
def inicio():
    return 'Sistema de cadastro de trens. '+\
        '<a href="/listar_trens">Listar Trens</a>'

@app.route("/listar_trens")
def listar_trens():
    
    trens = db.session.query(Trem).all()
    
    trens_json = [ x.json() for x in trens ]
    
    return jsonify(trens_json)
    
    resposta = jsonify(trens_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

app.run(debug=True)