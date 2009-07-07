#!/bin/bash

Help(){
	echo '============================'
	echo 'Help for downloadDependences'
	echo '============================'
	echo ''
	echo 'DESCRIPTION'
	echo '	This script download recursively all the dependencies of the'
	echo 'given packages.'
	echo ''
	echo 'SYNOPSIS'
	echo '	./downloadDependencies.sh PACKAGE1 PACKAGE2 ...'
	echo ''
	echo 'OPTIONS'
	echo '	-h, --help'
	echo '		show this short usage summary.'
	echo ''
	echo 'AUTHOR'
	echo '	Hugo Henriques Maia Vieira'
	echo ''
	echo 'Created on 09/04/2009'
}

downloadPackageDependences(){
	mkdir $package
	#Make an copy of downloadDependencies.py to execute it in the $package folder
	cp downloadDependencies.py $package
	cd $package

	if aptitude download $package
	then
		#All the dependencies will go to the archive depends.txt
	    apt-rdepends $package > depends.txt
		#The $LANG is an environment variable that inform the language of the Operational System.
	    python downloadDependencies.py $LANG
	    rm downloadDependencies.py
		#Setup the permission to execute the script
	    chmod u+x depends.sh
	    ./depends.sh
		rm depends.sh
		cd ..
	else
	    cd ..
	    rm -R $package
	fi
}

for package in $*
do
	if [ `echo $package | grep ^-` ] #Regex to catch everything that initiate with -, like -h, --help and etc
	then
		Help;
	else
		downloadPackageDependences;
	fi
done

