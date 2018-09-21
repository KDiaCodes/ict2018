from subprocess import Popen

number = int(input("please enter a number "))

if number % 2 == 0:
    print("it's even")
else:
    print("it's odd")

Popen('run.bat', cwd=r'Desktop')
