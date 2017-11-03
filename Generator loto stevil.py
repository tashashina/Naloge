import random


def main():
    print("Dobrodosli v loto generatorju nakljucnih stevil!")

    seznam_nakljucnih_stevil = []
    stevilo_nakljucnih_stevil = int(raw_input("Vnesi stevilo nakljucno izbranih stevil od 1 do 39: "))

    for x in range(stevilo_nakljucnih_stevil):
        while True:
            random_num = random.randint(1, 39)

            if random_num in seznam_nakljucnih_stevil:
                continue

            seznam_nakljucnih_stevil.append(random_num)
            break

    s = 0

    for item in seznam_nakljucnih_stevil:
        s += 1
        print str(s) + " " + str(item)

if __name__ == "__main__":
    main()
