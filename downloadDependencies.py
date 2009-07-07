# -*- coding: utf-8 -*-
'''
Created on 09/04/2009

@author: Hugo Henriques Maia Vieira
'''
import re
import os

#Receive the environment variable $LANG that inform the language of the Operational System.
language = os.environ['LANG']

def createDepensScript():
    original = open('depends.txt','r')
    modified = open('depends.sh', 'a')
    #Add the line to create a shell script
    modified.write('#!/bin/bash\n')
    #Just to control the "while" on the functions. When depends == '', that is the end of the archive.
    depends = 'not empty'
    while depends != '':
        depends = original.readline()
        if re.findall(r'^ ', depends):  #Find the lines that iniciate by a space
            if language.find('pt') == 0:
                depends = re.sub(r'  Pré-Depende:|  Depende:', 'aptitude download', depends)
            elif language.find('en') == 0:
                depends = re.sub(r'  Pre-Depends:|  Depends:', 'aptitude download', depends)
            depends = re.sub(r'\(>=.*\)', '', depends) #Remove the version >=
            depends = re.sub(r' \(= ', '=', depends) #Freeze the version =
            depends = re.sub(r'\)', '', depends) #Just complement of the regex above
            modified.write(depends)
    original.close()
    modified.close()


if (language.find('pt') == 0) or (language.find('en') == 0):
    createDepensScript()

else:
    print "\n\tbash: The script downloadDependencies does not support the language of \
your operational system.\n\n\tYou can adapt the line:\
\n\n\t\t\"depends = re.sub(r'  Pre-Depends:|  Depends:', 'aptitude download', depends)\"\
\n\n\tof the archive downloadDependencies.py to the language of your operational system.\
\n\n\tFor this, just run on terminal:\
\n\n\t\tapt-rdepends apt-rdepends\
\n\n\tand see the pattern of the substitutes words to \"Pre-Depends\" and \"Depends\". Then, chance the \
words on the file."
