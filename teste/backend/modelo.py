from config import *

class Trem(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(254))
    numero = db.Column(db.String(254))
    ano = db.Column(db.String(254))

    
    def __str__(self):
        return str(self.id)+") "+ self.marca + ", " +\
            self.numero + ", " + self.ano
     
    def json(self): 
        return { 
            "id": self.id, 
            "marca": self.marca, 
            "numero": self.numero, 
            "ano": self.ano 
        }
