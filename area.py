from subprocess import Popen

def Check():
    if answer == "t":
        Triangle()
        return
    elif answer == "r":
        Rectangle()
        return
    else:
        return

def Triangle():
    base = float(input("please enter a base digit: "))
    height = float(input("please enter a height value: "))
    area = base * height * 0.5
    print(area)

def Rectangle():
    base = float(input("please enter a base digit: "))
    height = float(input("please enter a height value: "))
    area = base * height
    print(area)

print("Would you like to calculate the area of a triangle or rectangle? [t/r]")
answer = input()
Check()
Popen('run.bat', cwd=r'Desktop')
