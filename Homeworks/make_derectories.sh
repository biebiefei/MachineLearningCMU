#!/bin/sh

for i in {1..30}
do
	dir_name="Lecture"${i}
	#echo ${dir_name}
	mkdir ${dir_name}
	mkdir ${dir_name}/wa
	mkdir ${dir_name}/bao
done
