import os

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Input a number to compute the factiorial : "))

print(factorial(n)) 

input("Press enter to close")

os.system(r'start C:\Windows\System32\cmd.exe /c C:\Users\KENRICSA\Desktop\start.bat')



# check if the number is negative, positive or zero
