class USB:
    def poweron(self):
        pass

class FAN(USB):
    def poweron(self):
        print('wing~~')

class Cup(USB):
    def poweron(self):
        print('cool')

class Phone(USB):
    def poweron(self):
        print('charging...')

f = FAN()
f.poweron()

c = Cup()
c.poweron()

p = Phone()
p.poweron()
