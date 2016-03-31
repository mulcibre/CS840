@ECHO off
start "sam program" cmd.exe /k "(echo %DATE:/=-%@%TIME::=-% & ping -n 5 google.com & echo %DATE:/=-%@%TIME::=-%) >> stuttgart.txt & exit"