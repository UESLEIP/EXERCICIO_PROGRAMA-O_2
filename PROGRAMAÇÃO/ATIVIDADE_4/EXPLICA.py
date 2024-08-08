class Retangulo:
    def __init__(self):
        self.largura = 1.0
        self.altura = 2.0
    def area (self):
        return self.largura * self.altura
    def perimetro (self):
        return 2*self.largura + 2 * self.altura
    
ret1 = Retangulo ()
print(ret1.area())