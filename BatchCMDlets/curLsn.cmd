@echo off
echo. Current Lesson Loaded = 37, on Thu 10/08/2020
for /f "usebackq" %%A in (`dir /s *lsn37 /b `) do @echo. %%~pftzA | find ":"