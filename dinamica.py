# Exemplo 1
class Documento:
    def imprimir(self):
        print("Imprimindo...")

class PDF(Documento):
    def imprimir(self):
        print("Imprimindo PDF...")


# Exemplo 2
class Documento:
    def imprimir(self):
        print("Imprimindo...")

class DocumentoSeguro(Documento):
    def imprimir(self):
        raise Exception("Impressão bloqueada.")


# Exemplo 3
class Carro:
    def dirigir(self):
        print("Dirigindo...")

class Moto(Carro):
    def dirigir(self):
        print("Pilotando...")

































# GABARITO
# 1 - ✅ Pode substituir!
# 2 - ❌ Vai quebrar! Esperávamos imprimir, mas agora dá erro!
# 3 - ✅ Pode substituir! Mesmo que mude o nome da ação, o comportamento geral é mantido.