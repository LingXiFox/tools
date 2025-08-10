import time
import subprocess
import os

if __name__ == "__main__":
    print("正在重启.............")
    os.system("taskkill /F /IM cmd.exe")
    subprocess.Popen(['python', "CheckStart.py"])
    os.system("exit")
    exit()