#!/usr/bin/env python3

# generates input for the backend programs
# generates both random usernames and passwords
# usernames random alphabets
# passwords any character

import os
import sys
import random

userPassDict = {} # username password container
userTemp = ""
passTemp = ""

userRange = [5, 10] # range of username
passRange = [8, 14] # range of password

if len(sys.argv) > 1:
    n = sys.argv[1] # number of randos to create
else:
    print("Usage: {} NUMBER".format(sys.argv[0]))
    exit()
    
userLen = 0
passLen = 0

randChar = 0

# generate username character database
userVals = 'abcdefghijklmnopqrstuvwxyz1234567890'
userDict = dict()

# load username chars into dictionary
for i, c in enumerate(userVals):
    userDict[i] = c

# generate password character database
passVals = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!#$%&()*+,-./:;<=>?@[]^_`{|}~'
passDict = dict()

# load password chars into dictionary
for i, c in enumerate(passVals):
    passDict[i] = c

tempDict = {}

numba = int(n)
looper = 0

# had to use while loop for easy way to not increase iterator in case of repeated username
while looper < numba:
    userLen = random.randint(userRange[0], userRange[1]) # gen len of username
    
    username = ""
    password = ""
    for i in range(userLen): # gen rando username
        randChar = random.randint(0, len(userVals) - 1)
        username += userDict[randChar]

    if username in userPassDict: # if username already exists, try again
        continue

    passLen = random.randint(passRange[0], passRange[1]) # gen len of password
    
    for k in range(passLen): # gen rando password
        randChar = random.randint(0, len(passVals) - 1)
        password += passDict[randChar]

    userPassDict[username] = password # add username-passwd to dictionary
    looper = looper + 1

for u in userPassDict: # output nicely
    print("{} {}".format(u, userPassDict[u]))
