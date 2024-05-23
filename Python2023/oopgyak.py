class Ember:
    def __init__(self,vnev,knev):
        self.vnev=vnev
        self.knev=knev

    def __str__(self):
        return self.vnev+" "+self.knev


class diak(Ember):
    def __init__(self,vnev,knev,osztaly):
        self.osztaly=osztaly
        super().__init__(vnev,knev)
    def koszon(self):
        print("jonapot")

    def __str__(self):
        return super().__str__()+","+self.osztaly

e1=Ember("Kovács","Béla")
print(e1)
d1=diak("Nagy","Elemér","13.K")
d1.koszon()
print(d1)