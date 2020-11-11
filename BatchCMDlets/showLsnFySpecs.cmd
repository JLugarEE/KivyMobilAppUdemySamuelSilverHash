@echo off
echo.1) explore old files:  df *lsn2*   
echo.   OR  for /f "usebackq" %%A in (^`dir /s *lsn2* /b ^`) do ^@echo. %%~pftzA ^| find ":"
echo.2) Use name Littoral (Lsn_DB01) as below, but no space in name):
echo.      for /f "usebackq" %%A in (^`dir /s m*.py m*.kv v*.py db.py /b ^`) do ^@echo. %%~pftzA _Lsn_DB01 ^| find ":"
echo.3) to make command work as you need
echo.    I.E.  for /f "usebackq" %%A in (^`dir /s *lsn27* /b ^`) do ^@echo^.copy /y %%~pfA %%~pfnA  (^.^?^?)
REM 								echo.copy /y %~pfA %~pfA  *.??
echo.   NOTE: you can ruin existing needed files
