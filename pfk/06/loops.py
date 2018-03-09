#!/usr/bin/env python3
################################################################################
#   loops.py
#
#   <Executable Module Purpose>
#
#   17.07.2017  Created by:  rada
################################################################################

for x in range(0,5):
    print('%s: Hello!' % x)
    
print('\n')    
for x in range(5):
    print('%s: again Hello!' % x)
    
print('\n')    
for x in range(0,-5,-1):
    print('%s: Hello more!' % x)
    
print('\n') 
print(list(range(10,20)))

print('\n') 
games =['Minecraft', 'Roblox', 'GTA5', 'CSgo']
for i in range(0, len(games)):
    print(games[i])
    
print('\n') 
for game in games: print(game)

print('\n')
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for day in days_of_week: print(day)


# while
print('\nWhile loop')
step = 0
while(step < 10):
    print(step)
    step = step + 1