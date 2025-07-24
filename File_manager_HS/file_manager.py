# %%
import os

# run the user's program in our generated folders
os.chdir('module/root_folder')

while True:

    cmd = input("Input the command ")

    if cmd == "pwd":
        print(os.getcwd())

    if cmd == "quit":
        break