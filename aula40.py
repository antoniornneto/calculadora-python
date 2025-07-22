while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador:\n [+] Soma\n [-] Subtração\n [*] Multiplicação\n [/] Divisão\n')
    operadores_permitidos = '+-*/'
    numeros_validos = None
    float_1 = float(numero_1)
    float_2 = float(numero_2)
    
    try:
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos.')
        continue
    
    if operador not in operadores_permitidos:
        print('Precisa ser um operador válido: \n [+] Soma\n [-] Subtração\n [*] Multiplicação\n [/] Divisão\n')
        continue
        
    if len(operador) > 1:
        print('Digite apenas um operador: \n [+] Soma\n [-] Subtração\n [*] Multiplicação\n [/] Divisão\n')
        continue
    
    if operador == '+':
        soma = float_1 + float_2
        print(soma)
    elif operador == '-':
        subtracao = float_1 - float_2
        print(subtracao)
    elif operador == '*':
        multiplicacao = float_1 * float_2
        print(multiplicacao)
    elif operador == '/':
        divisao = float_1 / float_2
        print(divisao)
    else:
        'Você precisa inserir um operador válido: [+] [-] [*] [/]'
    
    sair = input('Digite [s] para sair ou [c] para continuar: ').lower().startswith('s')
    if sair:
        break