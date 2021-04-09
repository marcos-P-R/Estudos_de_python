def hello(nomes):
    for nome in nomes:
        print("Hello " + nome.upper())

def tipos_pizzas(*args):
    print(args)

def dic_nomes(primeiro, idade):
    nome_idade = {}
    nome_idade['primeiro_nome'] = primeiro
    nome_idade['idade'] = idade
    for chave, valor in nome_idade.items():
        nome_idade[chave] = valor

    return nome_idade 


nomes = ['Jessica', 'Ana', 'Dianna', 'Elivelton']

hello(nomes)
tipos_pizzas('Mussarela', 'Peperone', 'Calabresa')

print(dic_nomes('Alex', 38))