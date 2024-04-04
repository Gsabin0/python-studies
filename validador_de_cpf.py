cpf_completo = '49384770841'#'37696055003'
cpf = cpf_completo[:9]
mutiplicaveis = 10
soma = 0

for num in cpf:
    multiplicacao = int(num)*mutiplicaveis
    soma +=multiplicacao
    #print(multiplicacao)
    mutiplicaveis -= 1
#print(soma)
divisao = (soma * 10) % 11
primeiro_digito = divisao if divisao <= 9 else 0 
#print(primeiro_digito)

cpf_prim_digito = "".join([cpf, str(primeiro_digito)])
mutiplicaveis_dig_2 = 11
soma_dig2 = 0
for num in cpf_prim_digito:
    multiplicacao_dig2 = int(num)*mutiplicaveis_dig_2
    soma_dig2 +=multiplicacao_dig2
    #print(multiplicacao_dig2)
    mutiplicaveis_dig_2 -= 1
#print(soma_dig2)
divisao_dig2 = (soma_dig2 * 10) % 11
segundo_digito = divisao_dig2 if divisao_dig2 <= 9 else 0 
#print(segundo_digito)
cpf_prim_seg_digito = "".join([cpf_prim_digito, str(segundo_digito)])

if cpf_completo == cpf_prim_seg_digito:
    print(f'CPF Valido {cpf_prim_seg_digito}')
else:
    print(f'CPF Invalido {cpf_prim_seg_digito}')
