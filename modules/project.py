import os

def create_project(name):

    path = "./projects/" + name

    if not os.path.exists("projects"):
        os.mkdir("projects")

    os.mkdir(path)

    with open(path + "/main.py", "w") as f:
        f.write('print("Hello from project")')

    print("Project created:", name)
