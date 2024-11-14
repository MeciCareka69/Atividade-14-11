# ENTRADA DO USUÁRIO
print("DESCUBRA SEU NOME E SUA IDADE")

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))

print(f"Seu nome é {nome}, você tem {idade} anos.\n")

# CARDÁPIO PARA O USUÁRIO
def menu():
    print("Qual a boa pro fim de semana?")
    print("1 - Bebidas")
    print("2 - Nargas")

    opc_user = int(input("Insira o número da opção desejada: "))

    if opc_user == 1:
        print("Boa escolha! Vamos esquecer os problemas da semana!")

    elif opc_user == 2:
        print("Excelente! escolha uma boa essência, mas cuidado com o pulmão!")

    else:
     print("Escolha uma opção válida de 1 a 2")