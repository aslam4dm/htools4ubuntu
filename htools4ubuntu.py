from os import system as cmd
with open("ubuntu_install_list.txt", 'r') as f:
    tools = f.read().split("--------")[4].split("\n")
    for t in tools:
        if t == "" or t == "\n":
            pass
        else:
            cmd("sudo apt-get install {}".format(t))

# you'll need root
# this is an automated installer for tools which i like to be installed on ubuntu
