path = '/home/marcosp/Documentos/desenvolvimento/python_estudos/python_basico/excessoes/pi.txt'
with open(path) as file_object:
    contents = file_object.read()
    print(contents)

try:
    with open('py.txt') as arquivo:
        exibir = arquivo.read()
        print(exibir)
except FileNotFoundError:
    msg = 'Arquivo não encontrado'
    print(msg)

    