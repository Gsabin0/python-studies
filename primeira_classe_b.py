import json
from primeira_classe import Celular

with open('teste.json', 'r') as arquivo:
    dados_json = json.load(arquivo)
    c1 = Celular(**dados_json[0])
    c2 = Celular(**dados_json[1])

print(c1.__dict__)
print(c2.__dict__)

#for pessoa in pessoas:
#    pessoa = Celular(**pessoa)
#    print(pessoa.__dict__)