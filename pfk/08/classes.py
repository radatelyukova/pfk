#!/usr/bin/env python3
################################################################################
#   classes.py
#
#   <Executable Module Purpose>
#
#   20.07.2017  Created by:  rada
################################################################################

class Things:
    pass

class Inanimate(Things):
    pass

class Cars(Inanimate):
    pass

class Animate(Things):
    pass

class Animals(Animate):
    def breathe(self):
        print('breathing')
    def eat(self):
        print('eating')
    def move(self):
        print('moving')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young with milk')

class People(Mammals):
    def __init__(self, eyes_color = 'unknown', age = 0, sex = 'Vasya'):
        self.eyes_color = eyes_color
        self.age = age
        self.sex = sex
    
    def dance(self):
        print("I'm dancing...")
        for i in range(5):
            self.move()
            
    def find_food(self):
        self.move()
        print('I have found food!')
        self.eat()

    def speak(self):
        print('speaking')

    def wearing_dress(self):
        if (self.sex == 'female'):
            print("that's dress is very good")
            print ("I'm princes!")
        elif (self.sex == 'male'):
            print("I'm weak")
        else:
            print("You're Vasya!")
            
rada = People('brown', 10, 'female')
print(rada.eyes_color, rada.age)
rada.breathe()
rada.speak()

dasha = People('green', 37, 'female')
print(dasha.eyes_color, dasha.age)
dasha.feed_young_with_milk()
dasha.find_food()

evgeny = People()
print(evgeny.eyes_color, evgeny.age)
evgeny.dance()
evgeny.wearing_dress()