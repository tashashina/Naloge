number = int(raw_input("Vnesi stevilo med 1 in 100: "))

for i in range(number):

    if ((i+1) % 3 == 0) and ((i+1) % 5 != 0):
        print("fizz")
    elif((i+1) % 3 != 0) and ((i+1) % 5 == 0):
        print("buzz")
    elif ((i+1)%3==0) and ((i+1)%5==0):
        print("fizzbuzz")
    else:
        print(i+1)