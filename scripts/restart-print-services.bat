net stop spooler
timeout /t 5 /nobreak
del %windir%\System32\spool\PRINTERS\* /Q /F /S
timeout /t 5 /nobreak
net start spooler