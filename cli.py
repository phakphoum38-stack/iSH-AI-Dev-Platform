from modules.shell import run_shell
from modules.project import create_project
from modules.github import clone_repo

def start_cli():
    while True:

        cmd = input("AI-DEV> ")

        if cmd == "exit":
            break

        elif cmd.startswith("run "):
            run_shell(cmd[4:])

        elif cmd.startswith("create "):
            create_project(cmd[7:])

        elif cmd.startswith("clone "):
            clone_repo(cmd[6:])

        else:
            print("Command not found")
