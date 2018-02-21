class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def setData(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        return self.first+self.second
    def div(self):
        return self.first/self.second
    def mul(self):
        return self.first*self.second
    def sub(self):
        return self.first-self.second
    def remainder(self):
        return self.first%self.second
    def divider(self):
        return self.first//self.second

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(3,4)
print(a.add())
print(a.pow())
