# -*- coding: utf-8 -*-
class myError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
def say_nick(nick):
    if nick == "바보":
        raise myError("메루메-☆")
    print(nick)
try:
    say_nick("천사")
    say_nick("바보")
except myError as e:
    print(e)
