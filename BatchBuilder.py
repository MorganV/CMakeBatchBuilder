# A super simple script to build all CMake projects in a given directory.
# Usage: "python BatchBuilder.py [dir]"
# Example: "python BatchBuilder.py /mnt/c/Users/Morgan/Documents/CS3353_Repos"
import os
import subprocess
import sys

print("Building all CMake projects in directory: " + sys.argv[1])

projects = os.listdir(sys.argv[1])
print("Building " + len(projects) + " projects.")
os.chdir(sys.argv[1])
for proj in projects:
    os.chdir(proj)
    #print("Current Directory: " + os.getcwd())
    os.system('cmake CMakeLists.txt & make')
    os.chdir(sys.argv[1])
