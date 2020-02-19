import pandas as pd
import os
import sys


projName = 'pa01-memmgr-'


df = pd.read_csv('gitInfo.csv', index_col='Timestamp')
df['GitHub'] = df['GitHub'].str.lower()  # Convert usernames to lowercase

print("Submisison root dir: " + sys.argv[1])
print("Output root directory: " + sys.argv[2])
projects = os.listdir(sys.argv[1])
print("Renaming " + str(len(projects)) +
      " directories to match email addresses.")

os.chdir(sys.argv[1])

for proj in projects:
    # Get email from gitinfo

    ghUsername = proj.strip().lower()
    email = df[df.GitHub == ghUsername].Email.values
    if len(email) == 0:
        print(ghUsername + " didn't fill out the survey.")
    else:
        os.chdir(sys.argv[1])
        os.chdir(proj)
        # Remove temporary file stuff
        os.system("rm -rf CMakeFiles/")
        os.system("rm -rf .github/")
        os.system("rm -rf .git/")
        os.chdir("..")

        command = 'cp -r ' + proj + ' ' + sys.argv[2] + ' ' + email
        os.system(command[0])
