# Menor de dois números - 01

# def minimo (a, b):
#     if a < b:
#         return a 
#     else: 
#         return b 
# print(minimo(5,6))
# print(minimo(2, 1))
# print(minimo(7, 7))

# Verificação de número par - 02

# def par(numero):
#     return numero % 2 == 0 
# print(par(4))
# print(par(7))
# print(par(0))

# Área do circuito - 03 

# def area_circulo(raio):
#     pi = 3.14
#     return pi * raio ** 2 
# print(area_circulo(2))
# print(area_circulo(5))


# Volume da esfera - 04

# def volume_esfera(raio):
#     pi = 3.14
#     return (4 / 3) * pi * raio ** 3
# print(volume_esfera(3))
# print(volume_esfera(1))

# Soma recursiva - 05 

# def soma_recursiva(n):
#     if n == 1:
#         return n
#     else:
#         return n + soma_recursiva(n-1)
# print(soma_recursiva(5))
# print(soma_recursiva(1))

# Média aritmética dos n primeiros números - 06 

# def media_n(n):
#     return soma_recursiva(n) / n 
# print(media_n(5))
# print(media_n(10))

# Validação de Faixa númerica - 07 

# def valida_faixa(numero, minimo, maximo):
#     return minimo <= numero <= maximo

# print(valida_faixa(5, 1, 10))
# print( valida_faixa (15, 1, 10))
# print(valida_faixa(1,1, 10))

# Contagem de ocorrências em lista - 08

# def conta_ocorrencias (lista, valor): 
#     contador = 0 
#     for numero in lista:
#         if numero == valor: 
#             contador += 1
#     return contador
# print(conta_ocorrencias([1,2,3,2,4,2], 2))
# print(conta_ocorrencias([5,6,7], 1)) 

# Conversão Celsius para Fahrenheit - 09

# def conversao(celsius):
#     return (celsius * 1.8) + 32
# print(conversao(0))
# print(conversao(100))
# print(conversao(25))

# Média simples de três - 10 

# def media_tres(a, b, c):
#     return (a + b + c) / 3 
# print(media_tres(6, 8, 10))
# print(media_tres(5, 5, 5))

# Cálculo Fatorial - 11

# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n - 1)
# print(fatorial(5))
# print(fatorial(0))

# Contagem de vogais - 12 

# def conta_vogais(texto):
#     contador = 0 
#     vogais = "aeiou"
#     texto = texto.lower()
    
#     for letra in texto:
#         if letra in vogais:
#             contador += 1
#     return contador
# print(conta_vogais("Python"))
# print(conta_vogais("Unip"))

#Índice de Massa Corporal (IMC) - 13 

# def calculo_imc(peso, altura):
#     return peso / (altura ** 2)
# print(calculo_imc(70, 1.75))
# print(calculo_imc(80, 1.80))

# Potência recursiva - 14

# def potencia(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * potencia (a, b -1)
# print(potencia(2, 3))
# print(potencia(5, 0))

# Filtragem de números - 15 

def filtra_pares(lista):
    pares = []
    
    for numero in lista: 
        if numero % 2 

