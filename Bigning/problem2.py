import os

# Specify the directory you want to list
directory_path = '/Application'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)
