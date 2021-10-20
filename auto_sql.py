import subprocess
import pyautogui as pg
import time

# cmdを開く
pg.press("Win")
pg.typewrite("cmd")
pg.press("enter")
time.sleep(0.3)

# cd後にpsql.exeのパス
pg.typewrite("cd ../../Program Files")
pg.press("enter")
pg.typewrite("cd postgreSQL/13/bin")
pg.press("enter")

#time.sleep(0.5)

# psql.exe
pg.typewrite("psql.exe -U postgres -d shop")
pg.press("enter")
#time.sleep(0.5)
pg.typewrite("postgres")
pg.press("enter")
