import random


def main():
    print("Dobrodosli v loto generatorju nakljucnih stevil!")

    seznam_nakljucnih_stevil = []
    stevilo_nakljucnih_stevil = int(raw_input("Vnesi stevilo nakljucno izbranih stevil od 1 do 39: "))

    for x in range(stevilo_nakljucnih_stevil):
        random_num = random.randint(1, 39)
        seznam_nakljucnih_stevil.append(random_num)

    for item in seznam_nakljucnih_stevil:
        print item


if __name__ == "__main__":
    main()
