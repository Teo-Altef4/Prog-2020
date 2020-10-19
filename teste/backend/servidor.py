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

@app.route("/incluir_trem", methods=['post'])
def incluir_trem():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    try:
        novo = Trem(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e: 
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/excluir_trem/<int:trem_id>", methods=["delete"]) 
def excluir_trem(trem_id): 
   # preparar uma resposta otimista 
   resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 
   try: 
      # excluir o trem do ID informado 
      Trem.query.filter(Trem.id == trem_id).delete() 
      # confirmar a exclusão 
      db.session.commit() 
   except Exception as e: 
      # informar mensagem de erro 
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
   # adicionar cabeçalho de liberação de origem 
   resposta.headers.add("Access-Control-Allow-Origin", "*") 
   return resposta # responder!

app.run(debug=True)