@echo off
color 0a
title Python file selector by KDiaCoding
:top
echo ***************************************************************
echo.
echo Python file selector
echo.
echo ***************************************************************
echo.
echo Key: [1] Area
echo [2] odd or even
echo [3] prime number
echo [4] all prime numbers in a range
echo [5] factorial
echo [6] sort
echo [7] guess numero
echo [8] counting days
echo [9] 2050
echo.
echo [e] Exit
echo.
echo ***************************************************************
echo Enter the number of the website which you would like to go to:
echo.
set /p udefine=
echo.
echo ***************************************************************
cls
if %udefine%==1 CMD /c python area.py
if %udefine%==2 CMD /c python oddoreven.py
if %udefine%==3 CMD /c python primenumber.py
if %udefine%==4 CMD /c python primenumrange.py
if %udefine%==5 CMD /c python factorial.py
if %udefine%==6 CMD /c python sortarray.py
if %udefine%==7 CMD /c python guessnumero.py
if %udefine%==8 CMD /c python countingdays.py
if %udefine%==9 CMD /c python intwentyfifty.py
if %udefine%==e goto exit

exit

:exit
cls
echo ***************************************************************
echo.
echo Thank You for using Site Selector by KDiaCoding
echo.
echo ***************************************************************
pause
exit
