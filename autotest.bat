set PYTHONPATH=C:\Renesas\e2_studio\eclipse\runtimes\python\2.7.12_x86\Lib
set Path=C:\Renesas\e2_studio\eclipse\runtimes\python\2.7.12_x86;%Path%
cd %1
rl78-elf-gdb.exe --silent HardwareDebug\%2.x < tests\autorun.gdbcmd > tests\log\autotest_log.txt
type tests\log\autotest_log.txt
findstr "OK" tests\log\autotest_log.txt