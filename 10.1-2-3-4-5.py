with open("textywexty.txt") as file_object:
    contents = file_object.read()
print(contents)

filename = "textywexty.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line)

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())



contoonts = contents.replace('python', 'lua')
print(contoonts)

print('\n\n')
fylename = 'boogiewoogie.txt'
with open(fylename, 'w') as file_object:
    file_object.write("")

gnomio = 'repons.txt'
with open(gnomio, 'w') as file_object:
    file_object.write("")

while 1 == 1:
    entry = input('Input username.\n>')
    with open(fylename, 'a') as file_object:
        file_object.write(f"{entry}\n")
    print(f"Welconme, {entry}.")
    entri = input('Why do you like python?\n>')
    with open(gnomio, 'a') as file_object:
        file_object.write(f"{entri}\n")