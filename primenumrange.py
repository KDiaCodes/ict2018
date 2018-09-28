import os

r = int(input("Please enter an number: "))

for n in range(2, r):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print (n)
print
input("Press enter to close")

os.system(r'start C:\Windows\System32\cmd.exe /c C:\Users\KENRICSA\Desktop\start.bat')
