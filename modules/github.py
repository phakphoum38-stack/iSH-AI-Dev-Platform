import os

def clone_repo(url):
    print("Cloning:", url)
    os.system("git clone " + url)
