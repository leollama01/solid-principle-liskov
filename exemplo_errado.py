class Pato:
    def quack(self):
        print("Quack!")

    def nadar(self):
        print("Nadando no lago.")

class PatoRobotico(Pato):
    def quack(self):
        raise Exception("Esse pato não faz som.")

    def nadar(self):
        raise Exception("Esse pato não sabe nadar.")
