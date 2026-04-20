class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
        
    def showNumber(self):
        print(self.real,"i + ",self.imag,"j")
        
    def add(self, num2):
        newReal = self.real+num2.real
        newImag = self.imag+num2.imag
        return Complex(newReal,newImag)
        
num1 = Complex(4,5) 
num1.showNumber()
 
num2 = Complex(6,9) 
num2.showNumber() 

num3 = num1.add(num2)
num3.showNumber()
