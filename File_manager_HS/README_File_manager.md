# File Manager (Basic Version)

## Overview
This is a basic version of a command-line file manager that allows users to view their current working directory and exit the program. It serves as a foundation for a more comprehensive file management system.

## Features
- View current working directory with `pwd` command
- Exit the program with the `quit` command

## How It Works
1. The program starts in a specified root directory
2. It continuously prompts the user for commands
3. Based on the command entered, it performs the corresponding operation:
   - `pwd`: Prints the current working directory
   - `quit`: Exits the program

## Commands
| Command | Description |
|---------|-------------|
| `pwd` | Print Working Directory - shows the current directory path |
| `quit` | Exit the program |

## Usage Example
```
Input the command pwd
/module/root_folder
Input the command quit
```

## Skills Demonstrated
- Basic file system operations with the `os` module
- User input processing in a loop
- Command parsing and execution
- Working with file paths

## Requirements
- Python 3.6 or higher

## Future Enhancements
This basic version can be expanded to include:
- Directory navigation with `cd` commands
- Listing directory contents
- File operations (copy, move, delete)
- File size display in different formats