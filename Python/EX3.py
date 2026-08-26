n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
n3 = int(input("Informe o terceiro valor: "))

numeros = n1, n2, n3 

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"{maior_numero} é o maior número")
print(f"{menor_numero} é o menor número")