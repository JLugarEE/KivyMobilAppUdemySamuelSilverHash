@echo off
echo.Manual commands for db testing (cut n paste)...:
echo.python 
echo.
echo.Py$:
echo.^>^>^> from app.storage.db import Database 
echo.db = Database()
echo.
echo.user = ('userNameMakeYourOwn','neverPrintThisPwKeepSecret')
echo.db.add_user(user)
echo.db.auth_user(('aRealUserName','dumbyPassw')) REM this one is ok to print as it is a place holder
echo.
echo.task = ('firsTask', '2020/09/25 13:21')
echo.db.add_task(task)
echo.db.get_tasks()
echo.
echo.task = ['firsTask', '2020/09/25 15:22']
echo.db.update_task(task)
echo.db.update_task()
echo.db.delete_task('firsTask')


