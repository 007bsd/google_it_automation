#!/bin/bash

# shellcheck disable=SC2188
> oldFiles.txt

files=$(grep ' jane ' list.txt | cut -d ' ' -f3)
echo "$files"
for f in $files; do
 if [ -e $HOMES ]; then
  echo $HOME >> oldFiles.txt
 fi
done