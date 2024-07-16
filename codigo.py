class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Perro:
    peso = 30 # Peso promedio

    def __init__(self, nombre, peso, raza):
        self.nombre = nombre
        self.peso = peso
        self.raza = raza

    @classmethod
    def get_peso_promedio(self):
        return self.peso

miPerro = Perro("Firulais", 12, "callejero")
print(f"Mi perro pesa {miPerro.peso}")
print(miPerro.get_peso_promedio())


class complejo:
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def modulo(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    def suma(self, other):
        return complejo(self.real + other.real, self.imag + other.imag)
    def resta(self, other):
        return complejo(self.real - other.real, self.imag - other.imag)
    def multiplicacion(self, other):
        return complejo(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    # def division(self, other):
    #     return denominator = other.real ** 2 + other.imag ** 2
    #     return complex((self.real * other.real + self.imag * other.imag) / denominator, (self.imag * other.real - self.real * other.imag) / denominator)

n1= complejo(1,2)
n2= complejo(3,4)
print(n1.modulo())
print(n2.modulo())
print(n1.suma(n2))

