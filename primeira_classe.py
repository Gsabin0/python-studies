import json

class Celular:
    def __init__(self, nome, marca, bateria, ligado=False):
        self.nome = nome
        self.marca = marca
        self._bateria = bateria
        self.ligado = ligado
    #decorador
    def confere_ligado(func):
        def confere_nivel(self, *args, **kwargs):
            if self.bateria <= 0:
                self.ligado = False
            else:
                self.ligado = True
            return func(self, *args, **kwargs)
        return confere_nivel 

    @confere_ligado
    def ligar(self):
        if self.ligado:
            print("Celular ligado.")
        else:
            print("Sem bateria para ligar")
    
    @property #geter
    def bateria(self):
        return self._bateria
    
    @bateria.setter #seter
    def bateria(self, valor):
        self._bateria = valor
        

if __name__ == ('__main__'):
    c1 = Celular('Mi13', 'Xiaomi', 95)
    c2 = Celular('Mi15', 'Xiaomi', 0)
    c1.ligar()
    c2.ligar()
    c2.bateria = 10
    c2.ligar()
    print(c1.__dict__)
    print(c2.__dict__)
    celulares = [c1.__dict__, c2.__dict__]

    with open('teste.json', 'w+') as arquivo:
        json.dump(celulares, arquivo, indent=2)
