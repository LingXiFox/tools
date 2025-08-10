import os
from modules import FunctionLibs

def move_file_obj():
    setting = FunctionLibs.json_read(".\\UI-Config.json")

    save_path = setting["OutPutPath"]
    save_path = str(save_path)

    arg = "move"+" "+"*.xppOBJ" +" "+save_path
    os.system(arg)

def move_file_xpp():
    setting = FunctionLibs.json_read(".\\UI-Config.json")

    save_path = setting["OutPutPath"]
    save_path = str(save_path)

    arg = "move"+" "+"*.xpp" +" "+save_path
    os.system(arg)

def move_ncm():
    setting = FunctionLibs.json_read(".\\UI-Config.json")

    save_path = setting["OutPutPath"]
    save_path = str(save_path)

    arg = "move D:\\CloudMusic\\VipSongsDownload\\*" +" " + save_path
    os.system(arg)
