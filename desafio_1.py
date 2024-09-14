menu = ("[1]: SAQUE [2]: DEPOSITO [3]: EXTRATO [0] SAIR\n")

saque = 0
saldo = 1000
saque_total = 0
extrato = 0

limite = 501
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    option = input(menu)

    if option == "1":
        print("=====SAQUE=====")
        saque = float(input("Valor: "))

        if numero_de_saques >= LIMITE_DE_SAQUES:
            print("Você atingiu o número maxímo de saques no dia!")

        elif saque <= 0:
            print("Valor invalido! Tente novamente")  

        elif saque >= limite:
            print("Valor maxímo atingido!") 

        elif saque < saldo:
            saldo -= saque
            saque_total += saque
            print(f"Você sacou R$ {saque}")
            numero_de_saques = numero_de_saques + 1
            print(f"{numero_de_saques}")   
        else:
            print("Você não tem saldo suficiente.")  
            
              
    elif option == "2":
        print("=====DEPOSITO=====")
        deposito = float(input("Valor: "))
        if deposito > 0:
            saldo += deposito
            extrato += deposito
            print(f"Deposito efetuado: R$ {deposito}.")
        else:
            print("Valor invalido! Tente novamente.")    

    elif option == "3":
        print("=====EXTRATO=====")
        print(f"Seu saldo atual é de: R$ {saldo}.")
        print(f"\nVocê depositou: R$ {deposito}")
        print(f"Você sacou: R$ {saque}")
        
    elif option == "0":
        print("Obrigado por utilizar nosso aplicativo!")
        break

    else:
        print("ERROR#404")