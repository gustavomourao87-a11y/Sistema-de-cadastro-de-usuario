class Usuario:
    def __init__(self, nome, cpf):
        if not nome:
            raise ValueError("Nome não pode ser vazio.")

        if not cpf:
            raise ValueError("CPF não pode ser vazio.")

        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF deve conter exatamente 11 números.")

        self.nome = nome
        self.cpf = cpf

    def exibir_dados(self):
        return f"Nome: {self.nome} | CPF: {self.cpf}"