import random

secret = random.randint(1, 100)

while True:
    guess = int(input("1 dan 100 gacha son kiriting: "))

    if guess < secret:
        print("Kattaroq son kiriting")
    elif guess > secret:
        print("Kichikroq son kiriting")
    else:
        print("To‘g‘ri! 🎉")
        break
