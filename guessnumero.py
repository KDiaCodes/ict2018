import random
import os

lives = 6
hidden = random.randrange(1, 100)
print(hidden)
while lives > 0:
    guess = int(input("Please enter your guess: "))
    if guess == hidden:
        print("Hit!")
        input("Press enter to close")
        os.system(r'start C:\Windows\System32\cmd.exe /c C:\Users\KENRICSA\Desktop\start.bat')
        break
    elif guess < hidden:
        print("Your guess is too low")
        lives = lives - 1
        print("lives left: [",lives,"]")
    else:
        print("Your guess is too high")
        lives = lives - 1
        print("lives left: [",lives,"]")



if lives == 0:
    print("you lose")
    input("Press enter to close")
    os.system(r'start C:\Windows\System32\cmd.exe /c C:\Users\KENRICSA\Desktop\start.bat')
