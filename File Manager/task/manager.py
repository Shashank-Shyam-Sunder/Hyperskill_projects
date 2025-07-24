# %%
import os

# run the user's program in our generated folders
os.chdir('module/root_folder')
print("Input the command")


def lsdir_sorted(lst_dir):
    list_subdir = []
    list_files = []
    for item_list in lst_dir:
        if "." in item_list:
            list_files.append(item_list)
        else:
            list_subdir.append(item_list)

    list_files.sort()
    list_subdir.sort()

    list_dir_updated = list_subdir + list_files

    return list_dir_updated

def file_size_converter(file_size):
    if file_size < 1024:
        file_size = str(file_size) + "B"
    elif 1024 <= file_size < (1024 * 1024):
        file_size = int(file_size / 1024)
        file_size = str(file_size) + "KB"
    elif (1024 * 1024) <= file_size < (1024 * 1024 * 1024):
        file_size = int(file_size / (1024 * 1024))
        file_size = str(file_size) + "MB"
    elif file_size > (1024 * 1024 * 1024):
        file_size = int(file_size / (1024 * 1024 * 1024))
        file_size = str(file_size) + "GB"
    return file_size

while True:
    try:
        cmd =  input()
        if cmd == "pwd":
            print(os.getcwd())
        elif cmd == "cd ..":
            os.chdir(os.path.dirname(os.getcwd()))
            print(os.path.basename(os.getcwd()))
        elif cmd[:2] == "cd":
            os.chdir(cmd.split("cd ")[1])
            print(os.path.basename(os.getcwd()))
        elif cmd == "ls":
            list_dir = os.listdir()
            if list_dir:
                list_dir_sorted = lsdir_sorted(list_dir)
                for item in list_dir_sorted:
                     print(item)
            else:
                pass
        elif cmd == "ls -l":
            list_dir = os.listdir()
            if list_dir:
                list_dir_sorted = lsdir_sorted(list_dir)
                for item in list_dir_sorted:
                    if "." in item:
                        print(f"{item} {os.stat(item).st_size}")
                    else:
                        print(item)
            else:
                pass
        elif cmd == "ls -lh":
            list_dir = os.listdir()
            if list_dir:
                list_dir_sorted = lsdir_sorted(list_dir)
                for item in list_dir_sorted:
                    if "." in item:
                        file_size = file_size_converter(os.stat(item).st_size)
                        print(f"{item} {file_size}")
                    else:
                        print(item)
            else:
                pass
        elif cmd == "quit":
            break
        else:
            print("Invalid command")

    except FileNotFoundError:
        print("No such file or directory exists!")

    except IndexError:
        print("Invalid command!")

