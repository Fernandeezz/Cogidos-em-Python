class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado com sucesso.")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo disponível: R${self.saldo:.2f}")


contas = {}


def criar_conta():
    numero_conta = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(numero_conta, titular)
    contas[numero_conta] = conta
    print("Conta criada com sucesso.")


def realizar_operacao():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta not in contas:
        print("Conta não encontrada.")
        return

    conta = contas[numero_conta]
    operacao = input("Digite 'D' para depósito, 'S' para saque ou 'C' para consultar saldo: ")

    if operacao == 'D':
        valor = float(input("Digite o valor do depósito: "))
        conta.depositar(valor)
    elif operacao == 'S':
        valor = float(input("Digite o valor do saque: "))
        conta.sacar(valor)
    elif operacao == 'C':
        conta.consultar_saldo()
    else:
        print("Operação inválida.")


while True:
    print("\n==== Sistema Bancário ====")
    print("1. Criar conta")
    print("2. Realizar operação")
    print("3. Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        criar_conta()
    elif opcao == '2':
        realizar_operacao()
    elif opcao == '3':
        break
    else:
        print("Opção inválida.")

print("Sistema encerrado.")
