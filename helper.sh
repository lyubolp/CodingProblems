#!/bin/bash
git pull;
echo $1 $2;
mkdir "$1" && cd "$1";

touch $2;
vim $2;

current_date=$(date +"%d%m%Y")
git add $2 && git commit -m "Daily coding "$current_date && git push
