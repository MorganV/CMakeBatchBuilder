import pandas as pd
import os
import sys


projName = 'pa01-memmgr-'



df = pd.read_csv('gitInfo.csv', index_col='ID')
df['GitHub'] = df['GitHub'].str.lower()  # Convert usernames to lowercase

print("Submisison root dir: " + sys.argv[1])
projects = os.listdir(sys.argv[1])
print("Renaming " + str(len(projects)) + " directories to match email addresses.")

os.chdir(sys.argv[1])

for proj in projects:
    # Get email from gitinfo
    os.chdir(proj)
    os.system("rm -rf .github/")
    os.system("rm CMakeCache.txt")
    os.system("rm -rf CMakeFiles/")
    os.system("rm Makefile")
    
    os.chdir("..")
    continue
    ghUsername = proj.strip().lower()
    email = df[df.GitHub == ghUsername].Email.values
    if len(email) == 0:
          print(ghUsername + " didn't fill out the survey.")
    else:
          print("Rename " + proj + " to " + email[0])
          command = 'mv ' + proj + ' ' + email
          os.system(command[0])
          
