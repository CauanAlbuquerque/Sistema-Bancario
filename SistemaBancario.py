def menu():
    return """
    ======================//======================
    Seja bem vindo(a) ao banco digital!
    Qual operação deseja executar?

    [d] depositar
    [s] sacar
    [e] Extrato
    [q] Sair
    ======================//======================
    """

def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"deposito de R${valor}\n"
    return saldo, extrato
    

def sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > saldo:
        return "Você não tem dinheiro suficiente na conta! "

    else: 
        if valor > limite:
            return f"O máximo que se pode sacar em uma operação é: {limite}, tente novamente!"
                
        else:
            saldo -= valor
            print("Saque efetuado")           
            extrato += f"Saque de R${valor}\n"
            numero_saques += 1
            return saldo, extrato, numero_saques

    
def exibir_extrato(saldo, extrato):
    print(extrato if extrato else "Nenhuma movimentação realizada.")
    print(f"Saldo atual: R${saldo:.2f}")
            

def main(): 
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3


    while True:
        opcao = input(menu())
    
    
        if opcao == "d":
            valor = float(input("Digite o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        
        elif opcao == "s":
            valor = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)
            if numero_saques == LIMITE_SAQUES:
                break
            print("Saque efetuado! ")
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        
            
        elif opcao == "q":
            break
        
        
        else:
            print("Digite uma opção válida!")
        
        
        
        print(f"Seu saldo é de: {saldo}")
        

main()