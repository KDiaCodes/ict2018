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
echo [4] Facebook - Social Networking
echo [5] Myspace - Social Networking
echo [6] CNN - News
echo [7] Weather - Weather
echo [8] WikiHow - A How-To Website
echo [9] Instructables - A How-To Website
echo [10] YouTube - Online Videos
echo [11] Answers - Online Encyclopedia
echo [12] Wikipedia - Online Encyclopedia
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
if %udefine%==4 start www.facebook.com
if %udefine%==5 start www.myspace.com
if %udefine%==6 start www.cnn.com
if %udefine%==7 start www.weather.com
if %udefine%==7 start www.wikihow.com
if %udefine%==9 start www.instructables.com
if %udefine%==10 start www.youtube.com
if %udefine%==11 start www.answers.com
if %udefine%==12 start www.wikipedia.com
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
