class first_class(object,firstVal):
    def __init__(self):
        self.firstVal = firstVal
        firstVal = 5
        print(firstVal)

    def squared(self,valx):
        self.valx = valx
        return valx ** 2

print(first_class.squared(4))
