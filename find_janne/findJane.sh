#!/bin/bash

> oldFiles.txt

files=$(grep " jane " list.txt | cut -d' ' -f3 | cut -d'/' -f3 )
for f in $files; do
  if [ -e $HOME ]; then
    echo $HOME/$f >> oldFiles.txt;
  fi
done
