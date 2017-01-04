#!/usr/bin/python
# Date: 2017/3/4 11:35am
# Filename: state_mode.py

class State:
    def write_something(self):
        pass

class Work:
    def __init__(self):
        self.hour = 9
        self.current = ForenoonState()

    def set_state(self, temp):
        self.current = temp

    def write_something(self):
        self.current.write_something(self)

class NoonState(State):
    def write_something(self, w):
        print "noon work."
        if(w.hour < 13):
            print "fun"
        else:
            print "need to rest."

class ForenoonState(State):
    def write_something(self, w):
        if(w.hour < 12):
            print "morning working"
            print "energetic"
        else:
            w.set_state(NoonState())
            w.write_something()

if __name__ == "__main__":
    mywork = Work()
    mywork.hour = 9
    mywork.write_something()
    mywork.hour = 14
    mywork.write_something()
