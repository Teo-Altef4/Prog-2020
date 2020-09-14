from modelo import *
import os

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    # teste da classe Trem
    trem1 = Trem(marca = "GE Dash", numero = "8-32B", 
        ano = "1989")
    trem2 = Trem(marca = "GE Dash", numero = "8 Series", 
        ano = "1994")
    trem3 = Trem(marca = "Bavariam", numero = "D X", 
        ano = "1890")
    trem4 = Trem(marca = "Prussiam", numero = "G 8", 
        ano = "1913")
    trem5 = Trem(marca = "Prussiam", numero = "G 12", 
        ano = "1924")
    trem6 = Trem(marca = "DBAG", numero = "Class 146", 
        ano = "2002")
    trem7 = Trem(marca = "DR", numero = "Class E 251", 
        ano = "1965")
    # persistir
    db.session.add(trem1)
    db.session.add(trem2)
    db.session.add(trem3)
    db.session.add(trem4)
    db.session.add(trem5)
    db.session.add(trem6)
    db.session.add(trem7)
    db.session.commit()

    print(trem1.json())
    print(trem2.json())
    print(trem3.json())
    print(trem4.json())
    print(trem5.json())
    print(trem6.json())
    print(trem7.json())
