#!/bin/bash -x
chars rs.txt
./find_junk.py > torm.txt
grep -v -w -F -f torm.txt rs.txt > rs_fixed.txt
