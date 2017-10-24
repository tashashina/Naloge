import random


def main():
    secret = random.randint(1, 30)
    print ("Ugani celo stevilo od 1 do 30")

    while True:
        guess = raw_input("Vnesi stevilo: ")

        if guess.isdigit():
            guess = int(guess)
            if guess == secret:
                print("Cestitam, uganil si stevilo!")
            else:
                print("Nisi uganil stevila!")
        else:
            print("Nisi vnesel celega stevila! ")

        new = raw_input("Zelis nadaljevati? (Da/Ne): ")

        if new.lower() == "da":
            continue
        else:
            print ("Iskano stevilo je " + str(secret))
            break

    print "END"


if __name__ == "__main__":
    main()