import os

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

os.system(r'start C:\Windows\System32\cmd.exe /c C:\Users\KENRICSA\Desktop\start.bat')
