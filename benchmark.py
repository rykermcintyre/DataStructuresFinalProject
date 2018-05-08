#!/usr/bin/env python

import subprocess
import time

BACKENDS=[
	"linkedlist",
	"rbtree",
	"sepchain",
]
NITEMS = [1, 10, 100, 200, 300, 400, 500]

print ('| BACKEND         | NITEMS    | CREATE            | LOGIN             |')
print ('|-----------------|-----------|-------------------|-------------------|')

for nitem in NITEMS:
    p1=subprocess.Popen(["./load2", str(nitem)])
    subprocess.Popen.wait(p1)
    for backend in BACKENDS:
        sp = subprocess.Popen("./continuous", stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=25)
        with open("database.txt", "r") as d:
            line = d.readline()
            while line:    
                line = line.rstrip().split(" ")
                #print(line[0], line[1], line[2])
                print >> sp.stdin, line[0]
                print >> sp.stdin, line[1]
                print >> sp.stdin, line[2]
                sp.stdin.flush()
                line  = d.readline()
        totCreateTime = 0
        for i in range(1, 2):
            start = time.time()
            print >> sp.stdin, "insert"
            print >> sp.stdin, "user" + str(i)
            print >> sp.stdin, "password" + str(i)
            sp.stdin.flush()
            end = time.time()
            totCreateTime = totCreateTime + (end - start)
        avgCreateTime = totCreateTime / 10.
        totLoginTime = 0
        for j in range(1, 2):
            start = time.time()
            print >> sp.stdin, "insert"
            print >> sp.stdin, "user" + str(i)
            print >> sp.stdin, "password" + str(i)
            sp.stdin.flush()
            end = time.time()
            totLoginTime = totLoginTime + (end - start)
        avgLoginTime = totLoginTime / 10.
        print("| {:<15} | {:<9} | {:<17} | {:<17} |".format(backend, nitem, avgCreateTime, avgLoginTime))            
