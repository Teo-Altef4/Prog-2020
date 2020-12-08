from config import *
from modelo import Fabricante, Trem, Estado_Cliente

@app.route("/")
def inicio():
    return 'Sistema de cadastro de trens. '+\
        '<a href="/listar/Trem">Listar Trem</a>'
#ROTA PARA LISTAR TRENS
@app.route("/listar/<string:classe>")
def listar(classe):
    dados = None
    if classe == "Fabricante":
        dados = db.session.query(Fabricante).all()
    elif classe == "Trem":
        dados = db.session.query(Trem).all()
    elif classe == "Estado_Cliente":
        dados = db.session.query(Estado_Cliente).all()
    lista_jsons = [x.json() for x in dados]
    resposta = jsonify(lista_jsons)
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