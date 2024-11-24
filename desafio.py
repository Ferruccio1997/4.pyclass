CONSTANTE_BONUS = 1000
funcionarios: list[dict] = []


def cadastra_funcionario(banco: list) -> list:
    nome_valido: bool = False
    salario_valido: bool = False
    bonus_valido: bool = False

    while nome_valido == False or salario_valido == False or bonus_valido == False:

        nome: str = input('Digite seu nome: ')
        
        if nome.isdigit():
            print('Digitou um numero no nome. Digite um nome valido!')
            nome_valido = False
        elif len(nome) == 0:
            print('Digite um nome válido!')
            nome_valido = False
        elif nome.isspace():
            print('Digitou somente espaço. Digite um nome valido!')
            nome_valido = False
        else:
            nome_valido = True
            for funcionario in banco:
                if funcionario['Nome'] == nome:
                    print('Nome ja cadastrado no banco!')
                    nome_valido = False
                    break
            if nome_valido == False:
                break        
            try:
                salario: float = round(float(input('Digite seu salario: ')),2)
                bonus: float = round(float(input('Digite o bonus: ')),2)
                if salario > 0 and bonus >= 0:
                    print('Salario e bonus validos!')
                    salario_valido = True
                    bonus_valido = True
                else:
                    print('Salario e bonus nao validos!')
                    salario_valido = False
                    bonus_valido = False
            except ValueError:
                salario_valido = False
                bonus_valido = False
    

    if nome_valido == True and salario_valido == True and bonus_valido == True:
        funcinario = {
            'Nome': nome,
            'Salario': salario,
            'Bonus': bonus
        }
        banco.append(funcinario)
        print('Funcionario cadastrado!')
    return banco

def calcula_beneficio(banco: list) -> list:
    for funcionario in banco:
        funcionario['Bonificacao'] = CONSTANTE_BONUS + round(funcionario['Salario'] * funcionario['Bonus'],2)

    return banco

def apresenta_info(banco: list, nome: str) -> str:
    mensagem = 'Funcionario nao cadastrado no banco!'

    for funcionario in banco:
        if funcionario['Nome'] == nome:
            mensagem = f'Ola {nome}, tudo bem? \n Seu salário é R${funcionario['Salario']} e com o percentual de {funcionario['Bonus']}% o se bonus é R${funcionario['Bonificacao']}'

    return mensagem

i = int(input('\nDigite 1 para cadastro \nDigite 2 para calculo de beneficio \nDigite 3 para apresentar informacao \nDigite 0 para sair: '))
while i != 0:
    if i == 0:
        break
    elif i == 1:
        cadastra_funcionario(funcionarios)
    elif i == 2:
        calcula_beneficio(funcionarios)
    elif i == 3:
        nome = input('Digite o nome a pesquisar: ')
        print(apresenta_info(funcionarios, nome))
    else:
        print('Numero invalido!')
    i = int(input('\nDigite 1 para cadastro \nDigite 2 para calculo de beneficio \nDigite 3 para apresentar informacao \nDigite 0 para sair: '))