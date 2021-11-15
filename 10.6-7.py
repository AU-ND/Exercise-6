def intecheck(num):
    try:
        int(num)
    except(ValueError):
        print("Wow I've had this code lying around forever, and that's not a number.")
        return 0

while 1 == 1:
    clear = 1
    number1 = input('Input a number\n>')
    if intecheck(number1) == 0:
        clear = 0
    if clear == 1:
        number2 = input('Input a number\n>')
        if intecheck(number2) == 0:
            clear = 0
        if clear == 1:
            result = int(number1) + int(number2)
            print(result)