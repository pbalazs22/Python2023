class uzenet:
    def __init__(self,sor1,sor2):
        #"2 15"
        self.nap=int(sor1.split(" ")[0])
        self.amator=int(sor1.split(" ")[1])

        self.szoveg=sor2

    def farkasVan(self):
        return "farkas" in self.szoveg