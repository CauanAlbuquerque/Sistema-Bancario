def menu():
    return """
    ======================//======================
    Seja bem vindo(a) ao banco digital!
    Qual operação deseja executar?

    [c] cadastrar usuario
    [d] depositar
    [s] sacar
    [e] Extrato
    [q] Sair
    ======================//======================
    """

def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"Deposito de R${valor}\n"
    return saldo, extrato
    

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
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

    
def exibir_extrato(saldo, *, extrato):
    print(extrato if extrato else "Nenhuma movimentação realizada.")
    print(f"Saldo atual: R${saldo:.2f}")
            

def criar_usuario(usuarios):
    cpf = input("Insira seu CPF (somente com numeros) -> ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("Já existe um usuário com esse cpf ")
        return 
    
    nome = input("Insira seu nome completo -> ")
    data_nascimento = input("Insira sua data de nascimento -> ")
    endereco = input("Insira seu endereço com o formato: logradouro, nro - bairro - cidade/sigla estado -> ")
    
    usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso! ")
    
def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if "cpf" == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    

def main(): 
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    
    

    while True:
        opcao = input(menu())
    
        if opcao == "c":
            criar_usuario(usuarios)
                        
        elif opcao == "d":
            valor = float(input("Digite o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        
        elif opcao == "s":
            valor = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite, 
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES)
            
            print(saldo)
            
            if numero_saques == LIMITE_SAQUES:
                break
            
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
            
        elif opcao == "q":
            break
        
        
        else:
            print("Digite uma opção válida!")
        
        
        
main()