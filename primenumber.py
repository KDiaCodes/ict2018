import os

num = int(input("Enter a number: "))

if num > 1:
   for i in range(2, num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num, "is a prime number")

else:
   print(num, "is not a prime number")

input("Press enter to close")

os.system(r'start C:\Windows\System32\cmd.exe /c C:\Users\KENRICSA\Desktop\start.bat')
