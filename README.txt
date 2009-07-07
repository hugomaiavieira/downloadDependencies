=====================================
Using the downloadDependencies script
=====================================

The script is composed by two archives: downloadDependencies.py and
downloadDependencies.sh. Both must be in the same folder.
To run the scrip, run the following code on the terminal:

 $ ./downloadDependencies.sh nameOfThePackages

The names of the packages must be separated by a space.

The result of the script execution is a folder with the name of the package.
In this folder you will find all of the dependencies of the packages and the
package itself. You will find too the archive depends.txt. That archive 
contains the tree of dependencies and you will use it to know the order of the 
packages instalation.

Dependencies
------------

To use the downloadDependencies script, you have to get the apt-rdepends 
package. For this, run the following code on the terminal:

 $ apt-get install apt-rdepends


Author
------

Hugo Henriques Maia Vieira

09/04/09
