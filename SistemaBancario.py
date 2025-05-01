menu = """
======================//======================
Seja bem vindo(a) ao banco digital!
Qual operação deseja executar?

[d] depositar
[s] sacar
[e] Extrato
[q] Sair
======================//======================

"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    
    if opcao == "d":
        deposito = float(input("Digite o valor que deseja depositar: "))
        saldo =+ deposito
        print(f"Operação bem sucedida, seu novo saldo é de: {saldo}")
        extrato += f"deposito de R${deposito}\n"
        
        
    elif opcao == "s":
        saque = float(input("Digite o valor que deseja sacar: "))
        if saque > saldo:
            print("Você não tem dinheiro suficiente na conta! ")

        else: 
            if saque > 500:
                print(f"O máximo que se pode sacar em uma operação é: {limite}")
                
            else:
                saldo =- saque
                print("Saque efetuado")           
                extrato += f"Saque de R${saque}\n"
            
    elif opcao == "e":
        print(extrato)
    
        
    elif opcao == "q":
        break
    
    
    else:
        print("Digite uma opção válida!")
    
    
    
    print(f"Seu saldo é de: {saldo}")
    
    if numero_saques == LIMITE_SAQUES:
        print("Limites de saque atingido! ")
    