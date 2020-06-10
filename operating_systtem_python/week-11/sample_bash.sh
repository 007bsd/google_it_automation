#!/bin/bash

echo "starting time is : $(date)"
echo

echo "Uptime"
uptime
echo

echo "FREE"
free
echo

echo "WHO"
who
echo

echo "ending time is : $(date)"
echo


grep ' jane ' ~/data/list.txt
 grep ' jane ' ~/data/list.txt

 grep ' jane ' ~/data/list.txt | cut -d ' ' -f1,3

if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi
for i in 1 2 3; do echo $i; done

Rohit Hemant Pawar
Week 6 : Graded Assesment
Rohit Hemant PawarWeek 6 · 20 days ago

After running findJane.sh , i m getting 3 files as output. But it is expected to have only 2 . The problem is to find files that starts with name jane , and interpreter is also considering file with name janez_profile . I m stucked and dont knw how to resolve this . Please help !

my Code:-

#!/bin/bash

>oldFiles.txt

files=$(grep "jane" ../data/list.txt | cut -d '' -f3)

for f in $files; do

if [ -e $HOME$f ]; then

echo $HOME$f >>oldFiles.txt;

fi

done


#!/bin/bash

>oldFiles.txt

files=$(grep ' jane ' ../data/list.txt | cut -d ' ' -f3)
echo $files
for f in $files; do
 if [ -e $HOMES$f ]; then
  echo $HOME$f >> oldFiles.txt
  echo "text" >> oldFiles.txt
  echo "anothertext" >> oldFiles.txt
 fi
done

#!/usr/bin/env python3
import sys
import subprocess

f = open(sys.argv[1], "r")
for line in f.readlines():
  old_name = line.strip()
  new_name = old_name.replace("jane", "jdoe")
  subprocess.run(["mv", old_name, new_name])
f.close()
