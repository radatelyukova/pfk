#!/usr/bin/env python3
################################################################################
#   03_dictionaries.py
#
#   <Executable Module Purpose>
#
#   13.07.2017  Created by:  rada
################################################################################

currency = {'Россия': 'рубль', 'Америка': 'доллар'}
print(currency['Россия'])
print(currency.keys())
print(currency.values())
print(currency.items())
print(len(currency))

for key in currency:
    print(key, ':', currency[key])

for key, value in currency.items():
    print(key,': ', value)
