from pessoa_fisica import Pessoa_fisica

pessoa_um = Pessoa_fisica("12345678900", nome="Alan", idade="Soares")
pessoa_dois = Pessoa_fisica("33333333333", "Augusto", "Castro")

pessoa_dois._nome = "Julio"

print(pessoa_um.get_CPF())
print(pessoa_dois.get_nome())