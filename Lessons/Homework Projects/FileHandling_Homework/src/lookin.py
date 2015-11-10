""" Make a FileHandling_Homework project and assign it to your
Python2_Homework working set. In that project, write a module
containing a function to examine the contents of the current
working directory and print out a count of how many files have
each extension (".txt", ".doc", etc.)"""
import os
import glob

def print_lst():
    # One empty dict to rule them all
    broke_dct = {}
    #Glob collect the names
    glob_lst = glob.glob("*.*")
    #This checks if it's a file, if yes, adds to dict, else it doesn't
    for p_file in glob_lst:
        if os.path.isfile(p_file):
            ext = os.path.splitext(p_file)[1]
            if ext in broke_dct.keys():
                broke_dct[ext] += 1
            else:
                broke_dct[ext] = 1
        else:
            continue
    return broke_dct