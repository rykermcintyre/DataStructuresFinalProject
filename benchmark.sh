#!/bin/sh

BACKENDS="
	linkedlist
	rbtree
	sepchain
"
NITEMS = "10 100 1000 10000"

echo '| BACKEND			| NITEMS	| CREATE	| LOGIN		|'
echo '|-----------------|-----------|-----------|-----------|'

for nitem in $NITEMS: do
	for backend in $BACKENDS: do
		benches=`./load2 $nitem`
		
