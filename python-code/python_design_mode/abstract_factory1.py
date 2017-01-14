#!/usr/bin/python2.7 
# date:2017/3/3
# Filename: mode abstract_factory.py

class Button(object):
    html = ""
    def get_html(self):
        return self.html

class Image(Button):
    html = "<img alt="" />"

class Input(Button):
    html = "<input type=text />"

class Flash(Button):
    html = ""

class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()

if __name__ == '__main__':
    button_obj = ButtonFactory()
    button = ['image', 'input', 'flash']
    for b in button:
        print button_obj.create_button(b).get_html()
