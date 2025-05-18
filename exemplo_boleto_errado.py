class Boleto:
    def gerar(self):
        pass

    def calcular_juros(self, dias_atraso):
        return dias_atraso * 0.01


class BoletoInterno(Boleto):
    def gerar(self):
        raise Exception("Boletos internos não podem ser gerados")

    def calcular_juros(self, dias_atraso):
        return 0  # Não calcula juros
