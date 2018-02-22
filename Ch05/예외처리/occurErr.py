# -*- coding: utf-8 -*-

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print('슈우우우웅-')

eagle = Eagle()
eagle.fly()
