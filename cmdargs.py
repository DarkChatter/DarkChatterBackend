## This file is to demonstrate how to establish command line arguments in python
##
## There are three examples here: send, mode, and a generic argument
## You may pass these values to the program to make it run in different ways
## Each argument can be used in any order, and they do not depend on each other.
## You may use none, all, or any amount in between, but only one of each in a call.
##
##
## Example calls for this file:
##
## >python cmdargs.py --send abc
## string argument to be sent over wifi is: abc
## 
## >python cmdargs.py -s abc -g stuff
## string argument to be sent over wifi is: abc 
## generic argument to be used as an example is: stuff




import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-s", "--send", required=False,
	help="string to send in packet")

ap.add_argument("-m", "--mode", required=False,
        help="Mode in which to run the script")

ap.add_argument("-g", "--genericarg", required=False,
        help="Description of what the argument is for")

args = vars(ap.parse_args())

#arguments stored for later use in a program
stringtosend = args["send"]
selectedmode = args["mode"]
genericstorage = args["genericarg"] 

# proof that the arguments are accepted
if stringtosend:
	print("string argument to be sent over wifi is: {}".format(stringtosend))
if selectedmode:
	print("argument entered for delivery mode  is: {}".format(selectedmode))
if genericstorage:
	print("generic argument to be used as an example is: {}".format(genericstorage))
