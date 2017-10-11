secret = 7

guess = raw_input("Ugani celo stevilo: ")

if guess.isdigit():
    guess = int(guess)
    if guess == secret:
        print("Cestitam, uganil si stevilo!")
    else:
        print("Nisi uganil stevila!")
else:
    print("Nisi vnesel celega stevila! ")