#!/usr/bin/env python


import os, re, sys

# if their are less than 3 arguments then this usage statment is printed

if (len(sys.argv) < 3):
    print('''
usage:
{0} KEYWORD|REGULAREXPRESSION all|single

all- Searches through the entire file tree and if any matchs are found returns them.

	{0} /home/exampledir/example.txt all
    
single- Searches against only file and directory names and if any matches are found returns them.

	{0} file.txt single

    '''.format(sys.argv[0]))
    sys.exit(0)


# collecting all user input and current working directory
# also collects the mode that the program will run in
# uses .lower so that the 3rd argument is not case dependent
arg1 = (sys.argv[2]).lower()
userinput = sys.argv[1]
filepath = os.getcwd() # gets the current directory that the program is being run from


# defining the lists that will contain the valid directories and files
dirlist=[]
filelist=[]

# if the 3rd argument is "all" then the entire file path is checked for any matches
if arg1 =="all":

    for direct, dirname, files in os.walk(filepath):
	       # checks files for a match
	       for i in files: 
			  #uses os.path.join to build a absolute path to check for matches
		          if(re.search('''{0}'''.format(userinput),os.path.join(direct,i))):
				     # saving any matches to a list for printing later
			             filelist.append(os.path.join(direct,i))
				
	       # checks the directorys for a match
	       if (re.search('''{0}'''.format(userinput),direct)):
		# saving any matches to a list for printing later 
                dirlist.append(direct)

# if the 3rd argument is "single" then only the end file or directory is checked for matches
elif arg1 == "single":
    for direct, dirname, files in os.walk(filepath):

	       for i in files:
		          if(re.search('''{0}'''.format(userinput),i)):
				     # saving any matches to a list for printing later
			             filelist.append(os.path.join(direct,i))


	       if (re.search('''{0}'''.format(userinput),os.path.basename(direct))):
		# saving any matches to a list for printing later
                dirlist.append(direct)


# if a third argument is found but does not match all or single then it prints a usage statment and closes
else:

    print('''
usage:
{0} KEYWORD|REGULAREXPRESSION all|single

all- searches through the entire file tree and if any matchs are found returns them

	{0} /home/exampledir/example.txt all

single- searches against only file and directory names and if any matches are found returns them

	{0} file.txt single

    '''.format(sys.argv[0]))
    sys.exit(0)

# printing off any matches 


print("-----------------------------------------------")
print("These are the files that have been located.")
print("-----------------------------------------------")
# this prints the files that match your input
for file in filelist:
	print(file)

print("-----------------------------------------------")
print("these are the directories that have been found.")
print("-----------------------------------------------")
# this prints the directories that match your input
for direct in dirlist:
	print(direct)


# Layonthehorn
# This lab was pretty fun to build and then expand on later with extra arguments
# it can search for either single files and directorys or search the whole file path
# it uses 3 arguments 1: ./lab7.py is the program being run 2: KEYWORD|REGULAREXPRESSION is the object you are seaching for
# and 3: all|single is the search method that it will use
#
