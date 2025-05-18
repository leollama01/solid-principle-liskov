class Boleto:
    def gerar(self):
        pass

    def calcular_juros(self, dias_atraso):
        return dias_atraso * 0.01  # 1% ao dia

    def registrar_no_banco(self):
        pass


class BoletoBancoDoBrasil(Boleto):
    def gerar(self):
        print("Gerando boleto padrão Banco do Brasil")

    def registrar_no_banco(self):
        print("Registrando via API do Banco do Brasil")


class BoletoBradesco(Boleto):
    def gerar(self):
        print("Gerando boleto padrão Bradesco")

    def registrar_no_banco(self):
        print("Registrando via CNAB Bradesco")


# Aplicando na prática
def processar_boleto(boleto: Boleto):
    boleto.gerar()
    boleto.registrar_no_banco()

# Não importa se o boleto é do Banco do Brasil, Bradesco ou Santander — todos devem funcionar da mesma forma nesse processo.