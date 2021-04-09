cats = ['Tom', 'Tapioca', 'Happy', 'Garfield']

for cat in cats:
    print('The cat\'s name is: ' + cat)

num = list(range(1, 6))
numeros = []
for nu in num:
    potencia = nu ** num[nu - 1]
    numeros.append(potencia)
    print(str(nu) + " elevado a " + str(nu) + " = " + str(potencia))

print(numeros)
print(max(numeros))
print(sum(numeros))
print(min(numeros))