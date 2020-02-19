import pandas as pd
import os
import sys

df = pd.read_csv('gitInfo.csv')
df["GitHub"].str.lower()  # Convert usernames to lowercase


print("Submisison root dir: " + sys.argv[1])
projects = os.listdir(sys.argv[1])
print("Renaming " + str(len(projects)) +
      " directories to match email addresses.")
projName = 'pa01-memmgr-'
for proj in projects:
    # Get email from gitinfo
    ghUsername = proj.replace(projName, "").trim().lower()
    email = df[df.GitHub == ghUsername].Email
    print("Rename " + proj + " to " + email)
    #os.system("mv " + proj + " " + email)
