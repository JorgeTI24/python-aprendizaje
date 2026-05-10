import re

numeros = [
    "5622092850",
    "5516986733",
    "475869403928",
    "12345"
]

for numero in numeros:
    resultado = re.fullmatch("\d{10}", numero)

    if resultado:
        print(numero, "valido")

    else:
        print(numero, "invalido")




