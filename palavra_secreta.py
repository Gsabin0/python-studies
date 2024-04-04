from time import sleep

palavra_secreta = "cachorro"
letras_acertadas = ''
numero_tentativas = 0
while True:
    input_cliente = input('Digite uma letra: ')
    
    if input_cliente.isnumeric():
        print('Vc digitou um numero digite uma letra')
        continue

    if len(input_cliente) > 1:
        print('digiite apenas uma letra:')
        continue
    
    if input_cliente in palavra_secreta:
        letras_acertadas += input_cliente 
        numero_tentativas += 1
    palavra_secreta_crip = ''
    for troca_letra in palavra_secreta:
        if troca_letra in letras_acertadas:
            palavra_secreta_crip += troca_letra
        else:
            palavra_secreta_crip += '*'
    print(palavra_secreta_crip)
    if palavra_secreta == palavra_secreta_crip:
        print(f'vc acertou a palavra {palavra_secreta_crip} com {numero_tentativas} tentativas')
        letras_acertadas = ''
        numero_tentativas = '0'
        break  

    
    
    