#TODO composição
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor: 
    def __init__(self, nome):
        self.nome = nome
    

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        



c1 = Carro('Palio')
f1 = Fabricante('Fiat')
m1 = Motor('Fire')
c1.motor = m1
c1.fabricante = f1
print(c1.nome, c1.fabricante.nome, c1.motor.nome)

c2 = Carro('Doblo')
c1.motor = m1
c1.fabricante = f1
print(c2.nome, c1.fabricante.nome, c1.motor.nome)

c3 = Carro('Civic')
f3 = Fabricante('Honda')
m3 = Motor('Ice')
c3.motor = m3
c3.fabricante = f3
print(c3.nome, c3.fabricante.nome, c3.motor.nome)