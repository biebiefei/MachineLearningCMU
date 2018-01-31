#!/bin/sh

for i in {1..30}
do
	dir_name="Lecture"${i}
	#echo ${dir_name}
	mkdir ${dir_name} #make lecture directories
	mkdir ${dir_name}/wa #wawa's directory
	mkdir ${dir_name}/bao #baobao's directory
done
