import random

num = random.randint(1, 100)
count = 7
print("Guess the number (1 .. 100), you have 7 chances.")
while count > 0:
    guess = int(input("enter the number: "))
    if guess == num:
        print("Bingo")
        break
    count -= 1
    if guess > num:
        print("It's too large.")
    else:
        print("It's too small.")
    print("You have", count, "chances" if count > 1 else "chance now.")
if count == 0:
    print("You failed ...")
    print("The number is", num)