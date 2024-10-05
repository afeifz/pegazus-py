class ContaBancaria:
    _id_counter = 1

    def __init__(self, nome, cpf):
        self.id = ContaBancaria._id_counter  
        ContaBancaria._id_counter += 1  
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0  

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}')
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        elif valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}')

class Banco:
    def __init__(self):
        self.contas = []  

    def criar_conta(self, nome, cpf):
        nova_conta = ContaBancaria(nome, cpf)  
        self.contas.append(nova_conta)  
        print(f'Conta criada com sucesso! ID: {nova_conta.id}, Nome: {nova_conta.nome}, CPF: {nova_conta.cpf}')

    def exibir_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada.")
            return
        print("Contas cadastradas:")
        for conta in self.contas:
            print(f'ID: {conta.id}, Nome: {conta.nome}, CPF: {conta.cpf}, Saldo: R${conta.saldo:.2f}')


banco = Banco()


banco.criar_conta("João da Silva", "123.456.789-00")
banco.criar_conta("Maria Oliveira", "987.654.321-00")

banco.exibir_contas()


conta1 = banco.contas[0]
conta1.depositar(1500.00)
conta1.sacar(500.00)

conta2 = banco.contas[1]
conta2.depositar(2000.00)
conta2.sacar(2500.00)
