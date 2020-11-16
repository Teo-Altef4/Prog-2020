from modelo import *
import os

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    fabricante1 = Fabricante(nome = "GE Transportation", nacao = "Estado Unidos")
    fabricante2 = Fabricante(nome = "Royal Bavarian State Railways", nacao =  "Alemanha")
    fabricante3 = Fabricante(nome = "Prussian state railways", nacao = "Alemanha")
    fabricante4 = Fabricante(nome = "ADtranz", nacao ="Alemanha")
    fabricante5 = Fabricante(nome = "LEW Hennigsdorf", nacao = "Alemanha")
    fabricante6 = Fabricante(nome = "Baldwin Locomotive Works", nacao = "Estado Unidos")

    # teste da classe Trem
    trem1 = Trem(marca = "GE Dash", numero = "8-32B", 
        ano = "1989", fabricante_id = "1")
    trem2 = Trem(marca = "GE Dash", numero = "8 Series", 
        ano = "1994", fabricante_id = "1")
    trem3 = Trem(marca = "Bavariam", numero = "D X", 
        ano = "1890", fabricante_id = "2")
    trem4 = Trem(marca = "Prussiam", numero = "G 8", 
        ano = "1913", fabricante_id = "3")
    trem5 = Trem(marca = "Prussiam", numero = "G 12", 
        ano = "1924", fabricante_id = "3")
    trem6 = Trem(marca = "DBAG", numero = "Class 146", 
        ano = "2002", fabricante_id = "4")
    trem7 = Trem(marca = "DR", numero = "Class E 251", 
        ano = "1965", fabricante_id = "5")

    estado_cliente1 = Estado_Cliente(nome = "Pennsylvania",  trem_id = "1")
    estado_cliente2 = Estado_Cliente(nome = "Bavaria",  trem_id = "2")
    estado_cliente3 = Estado_Cliente(nome = "Prussia",  trem_id = "3")
    estado_cliente4 = Estado_Cliente(nome = "Suica",  trem_id = "4")
    estado_cliente5 = Estado_Cliente(nome = "Saxônia-Anhalt",  trem_id = "5")
    estado_cliente6 = Estado_Cliente(nome = "Minesota",  trem_id = "6")
    estado_cliente7 = Estado_Cliente(nome = "Gales",  trem_id = "7")
    
    # persistir
    db.session.add(fabricante1)
    db.session.add(fabricante2)
    db.session.add(fabricante3)
    db.session.add(fabricante4)
    db.session.add(fabricante5)
    db.session.add(fabricante6)
    
    db.session.add(trem1)
    db.session.add(trem2)
    db.session.add(trem3)
    db.session.add(trem4)
    db.session.add(trem5)
    db.session.add(trem6)
    db.session.add(trem7)

    db.session.add(estado_cliente1)
    db.session.add(estado_cliente2)
    db.session.add(estado_cliente3)
    db.session.add(estado_cliente4)
    db.session.add(estado_cliente5)
    db.session.add(estado_cliente6)
    db.session.add(estado_cliente7)

    db.session.commit()

    print(fabricante1.json()) 
    print(fabricante2.json())
    print(fabricante3.json())
    print(fabricante4.json())
    print(fabricante5.json())
    print(fabricante6.json())

    print(trem1.json())
    print(trem2.json())
    print(trem3.json())
    print(trem4.json())
    print(trem5.json())
    print(trem6.json())
    print(trem7.json())

    print(estado_cliente1.json())
    print(estado_cliente2.json())
    print(estado_cliente3.json())
    print(estado_cliente4.json())
    print(estado_cliente5.json())
    print(estado_cliente6.json())
    print(estado_cliente7.json())