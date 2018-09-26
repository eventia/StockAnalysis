#! /bin/bash
git add --all .
if [ "$1" = "" ]
then 
	git commit -m "stk.demo"
else
	git commit -m "$*"
fi
git push