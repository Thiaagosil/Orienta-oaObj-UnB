# meu_programa.py

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        return f"{self.nome} está comendo."
    
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.cor = cor

    def miar(self):
        return f"{self.nome} ({self.cor}) está miando."

meu_gato = Gato("Charlotte", "Branco")
print(meu_gato.comer())
print(meu_gato.miar())
