menu = """

Informe o serviço que deseja realizar:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("============ Depositar ============")

        valor = float(input("Informe o valor do depósito: ")) # Pede para o usuário informar um valor

        if valor > 0:
            saldo += valor # valor > 0, insere o depósito na conta

            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!") # Informa que a operação ocorreu com sucesso

            extrato += f"Depósito: R$ {valor:.2f}\n" # Adiciona o valor do depósito no extrato c/ 2 casas decimais

        else:
            print("Operação não realizada! O valor informado é inválido.")

    
    elif opcao == "s":
        print("============ Sacar ============")
        
        valor = float(input("Informe o valor do saque: ")) # Pede para o usuário informar um valor

        excedeu_saldo = valor > saldo # Verifica se há saldo disponível
        excedeu_limite = valor > limite # Verifica se já sacou a quantia máx permitida
        excedeu_saques = numero_saques >= LIMITE_SAQUES # Verifica se já realizou todos os saques disponíveis


        if excedeu_saldo:
            print("Operação não realizada! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação não realizada! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação não realizada! Número máximo de saques excedidos.")

        
        # Caso entre com valor válido e não atenda às condições acima...
        elif valor > 0:
            saldo -= valor # Realiza o decremento (saque)

            print(f"Saque de R$ {valor:.2f} realizado com sucesso!") # Informa que a operação ocorreu com sucesso

            extrato += f"Saque: R$ {valor:.2f}\n"  # Add o valor de saque ao extrato
            numero_saques += 1 # incremento no nº de saques

        else:
            print("Operação não realizada! O valor informado é inválido.")
              

    elif opcao == "e":
        print("\n============ Extrato ============")
        print("Não houve movimentações bancárias." if not extrato else extrato) # if ternário -> Verifica se o extrato está vazio (print msg), senão o extrato com as operações realizadas
        print(f"\nSaldo: R$ {saldo:.2f}") # Exibe o saldo
        print("====================================")
    
    elif opcao == "q": # while passa a ser false e encerra o programa
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


