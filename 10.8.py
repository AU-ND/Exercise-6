def filecheck(file):
    try:
        with open(file, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print("Sorry Mario, the File is in another Directory.")
        return 0

clear1 = 1
clear2 = 1

file1 = input('Input first file name.\n>')
if filecheck(file1) == 0:
    clear1 = 0
file2 = input('Input second file name.\n>')
if filecheck(file2) == 0:
    clear2 = 0

if clear1 == 1:
    with open(file1, 'r') as f:
        contents = f.read()
        print(contents)

if clear2 == 1:
    with open(file2, 'r') as f:
        contents = f.read()
        print(contents)