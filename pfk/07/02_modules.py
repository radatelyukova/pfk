#!/usr/bin/env python3
################################################################################
#   02_modules.py
#
#   <Executable Module Purpose>
#
#   19.07.2017  Created by:  rada
################################################################################

import time

print(time.time())
print(time.ctime())

import time as t
print('\nimport as')
print(t.ctime())

from time import * 
print('\nimport *')
print(ctime())

from time import sleep
sleep(3)
print('end!')

