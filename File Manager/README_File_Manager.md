# File Manager

## Overview
File Manager is a command-line application that allows users to navigate and explore the file system. It provides various commands for directory navigation, listing contents, and viewing file sizes in different formats.

## Features
- Navigate through directories using `cd` and `cd ..` commands
- View current working directory with `pwd` command
- List directory contents with `ls` command
- View detailed listings with file sizes using `ls -l`
- Display human-readable file sizes (KB, MB, GB) with `ls -lh`
- Error handling for invalid commands and non-existent files/directories
- Exit the program with the `quit` command

## How It Works
1. The program starts in a specified root directory
2. It continuously prompts the user for commands
3. Based on the command entered, it performs the corresponding file system operation:
   - `pwd`: Prints the current working directory
   - `cd ..`: Moves up one directory level
   - `cd <directory>`: Changes to the specified directory
   - `ls`: Lists all files and directories in the current directory
   - `ls -l`: Lists files with their sizes in bytes
   - `ls -lh`: Lists files with their sizes in human-readable format (KB, MB, GB)
   - `quit`: Exits the program
4. The program handles errors such as non-existent directories or invalid commands

## Commands
| Command | Description |
|---------|-------------|
| `pwd` | Print Working Directory - shows the current directory path |
| `cd ..` | Change Directory - move up one level to the parent directory |
| `cd <directory>` | Change Directory - move to the specified directory |
| `ls` | List - show all files and directories in the current location |
| `ls -l` | List Long - show files with their sizes in bytes |
| `ls -lh` | List Long Human-readable - show files with sizes in KB, MB, GB |
| `quit` | Exit the program |

## Usage Example
```
Input the command
pwd
/module/root_folder
Input the command
ls
Documents
Downloads
Pictures
file.txt
Input the command
cd Documents
Documents
Input the command
ls -lh
report.doc 15KB
presentation.ppt 1MB
Input the command
cd ..
root_folder
Input the command
quit
```

## Skills Demonstrated
- File system operations with the `os` module
- Directory navigation and file listing
- File size conversion (bytes to KB, MB, GB)
- Command parsing and execution
- Error handling with try/except blocks
- User input processing in a loop
- Sorting and filtering directory contents

## Requirements
- Python 3.6 or higher