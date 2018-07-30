#!/bin/bash

i=1
while [ "${i}" != "10" ];
do
	echo "executing for iteration - ${i}"
	sleep 2
	echo "sleep completed at iteration - ${i}"
	let i+=1
done
