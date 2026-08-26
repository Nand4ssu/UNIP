velocidade = int(input("Digite a velocidade do usuário: "))
if velocidade > 80:
    multa= 5 * (velocidade - 80)
    print(f"Você foi multado! A sua velocidade foi acima de 80km!, o valor da multa é de R$ {multa}")
else :
    print("Você está dentro da velocidade permitida!")