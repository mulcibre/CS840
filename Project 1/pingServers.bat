@ECHO off
ECHO Program started
start "stuttgart" cmd.exe /k "(echo %DATE:/=-%@%TIME::=-% & ping -n 600 www.uni-stuttgart.de.edu & echo %DATE:/=-%@%TIME::=-%) >> log4sfsu/stuttgart.txt & exit"
start "hamburg" cmd.exe /k "(echo %DATE:/=-%@%TIME::=-% & ping -n 600 www.uni-hamburg.de.edu & echo %DATE:/=-%@%TIME::=-%) >> log4sfsu/hamburg.txt & exit"
start "caltech" cmd.exe /k "(echo %DATE:/=-%@%TIME::=-% & ping -n 600 turing.caltech.edu & echo %DATE:/=-%@%TIME::=-%) >> log4sfsu/caltech.txt & exit"
start "daffodilvarsity" cmd.exe /k "(echo %DATE:/=-%@%TIME::=-% & ping -n 600 daffodilvarsity.edu.bd & echo %DATE:/=-%@%TIME::=-%) >> log4sfsu/daffodilvarsity.txt & exit"
start "kiev" cmd.exe /k "(echo %DATE:/=-%@%TIME::=-% & ping -n 600 www.imi.kiev.ua & echo %DATE:/=-%@%TIME::=-%) >> log4sfsu/kiev.txt & exit"
start "fujita" cmd.exe /k "(echo %DATE:/=-%@%TIME::=-% & ping -n 600 www.fujita-hu.ac.jp & echo %DATE:/=-%@%TIME::=-%) >> log4sfsu/fujita.txt & exit"
start "sapporo" cmd.exe /k "(echo %DATE:/=-%@%TIME::=-% & ping -n 600 www.sapporo-u.ac.jp & echo %DATE:/=-%@%TIME::=-%) >> log4sfsu/sapporo.txt & exit"
start "stanford" cmd.exe /k "(echo %DATE:/=-%@%TIME::=-% & ping -n 600 stanford.edu & echo %DATE:/=-%@%TIME::=-%) >> log4sfsu/standford.txt & exit"
ECHO Program terminated successfully
PAUSE



