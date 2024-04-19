menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

nome = input(f"""Olá! :) 
Por favor, nos informe seu nome!""")

print(f"Olá, {nome}. Obrigado por usar nosso Banco. Como posso te ajudar hoje?")

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha! Saldo suficiente.")

        elif excedeu_limite:
            print("Falha! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Falha! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha! O valor informado é inválido.")

    elif opcao == "3":
        print(f"\n================ EXTRATO {nome} ================")

        if not extrato:
            print("Não foram realizadas movimentações." )
        else:
            print(extrato)

        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==================================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, favor selecionar novamente a operação desejada.")
