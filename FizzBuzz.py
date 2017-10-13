number = int(raw_input("Vnesi stevilo med 1 in 100: "))

for i in range(1, number+1):

    if (i % 3 == 0) and (i % 5 != 0):
        print("fizz")
    elif(i % 3 != 0) and (i % 5 == 0):
        print("buzz")
    elif (i % 3 == 0) and (i % 5 == 0):
        print("fizzbuzz")
    else:
        print(i)