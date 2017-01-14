#!/usr/bin/python
# Date:2017/3/3 17:21
# Filename: adapter.py

class Adaptee(object):
    def concreteRequest(self,w):
        self.command = w
        print "The real concreteRequest is " + w

class Target(object):
    def request(self):
        pass

class Adapter(Target):
    def __init__(self,tAdaptee,w):
        self.command = w
        self.targetAdaptee = tAdaptee

    def request(self):
        self.targetAdaptee.concreteRequest(self.command)

if __name__ == "__main__":
    adaptee = Adaptee()
    Adapter = Adapter(adaptee,"sing a song")
    Adapter.request()
