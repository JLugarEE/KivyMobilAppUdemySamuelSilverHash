@echo off
echo.
echo for ^/f "usebackq" ^%%A in ^(^`dir /s m*.py m*.kv v*.py       /b ^`) do ^@echo.^%%A ^%%A_Lsn7
echo.for ^/f "usebackq" ^%%A in ^(^`dir /s m*.py m*.kv v*.py db.py /b ^`) do ^@copy ^%%A ^%%A_Lsn7
echo.
dir /s app\storage\db.py* | find /v "Volume" | find " "
