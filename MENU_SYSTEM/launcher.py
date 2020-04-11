import subprocess
import os

os.chdir("/home/pi/MENU_SYSTEM")

while True:
    print("Launching...")
    p = subprocess.Popen(["./start.sh"])
    ret = p.wait()
    print("It quit!")
    if ret != 0:
        break
