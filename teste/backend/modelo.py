from config import *

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    nacao = db.Column(db.String(254))

    def __str__(self):
        return str(self.id)+", " + self.nome + ", " +\
            self.nacao

    def json(self):
        return ({
            "id": self.id,
            "nome": self.nome,
            "nacao": self.nacao
        })

class Trem(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(254))
    numero = db.Column(db.String(254))
    ano = db.Column(db.String(254))
    fabricante_id = db.Column(db.Integer, db.ForeignKey(Fabricante.id))
    fabricante = db.relationship("Fabricante")

    def __str__(self):
        t = f"Trem {self.marca}"
        if self.fabricante_id != None:
            t += f"produzido pelo fabricante {self.marca} localizado em {self.nacao}"
            return t
    
    def json(self):
        if self.fabricante_id is None:
            return ({
                "id": self.id,
                "marca": self.marca,
                "numero": self.numero,
                "ano": self.ano
            })
        else:
            return ({
                "id": self.id,
                "marca": self.marca,
                "numero": self.numero,
                "ano": self.ano,
                "fabricante": self.fabricante.json()
            })

class Estado_Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    trem_id = db.Column(db.Integer, db.ForeignKey(Trem.id), nullable=False)
    trem = db.relationship("Trem")

    def __str__(self):
        return str(self.id)+", " + self.nome

    def json(self):
        return ({
            "id": self.id,
            "nome": self.nome,
            "trem": self.trem.json()
        })