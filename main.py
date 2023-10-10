import math

# Classe base abstrata (com abstração)
class Forma:
    def calcular_area(self):
        raise NotImplementedError("Método abstrato deve ser implementado nas subclasses")

# Subclasse que herda de Forma
class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Subclasse que herda de Forma
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio**2

# Função principal
def main():
    # Criar uma forma de retângulo
    retangulo = Retangulo(5.0, 4.0)

    # Calcular e imprimir a área do retângulo
    print("Área do Retângulo:", retangulo.calcular_area())

    # Criar uma forma de círculo
    circulo = Circulo(3.0)

    # Calcular e imprimir a área do círculo
    print("Área do Círculo:", circulo.calcular_area())

# Chamar a função principal
if __name__ == "__main__":
    main()
