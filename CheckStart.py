import os
import sys
import tkinter.messagebox
import argparse

#!测试库是否存在（和本程序无关库）
try:
    import tqdm
    import validators
    import Crypto
    import requests
    import werkzeug
    import PIL
except:
    print("必须安装下列工具：tqdm validators Crypto requests werkzeug")
    print("开始补齐依赖")
    os.system("pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/")
    print("补齐完成")

def Check_Files():
    WorkSpace = sys.path[0]
    dic={"files":[
                  #!main
                  ".\\UI-Config.json",
                  ".\\move_files.py",
                  ".\\main.py",
                  ".\\requirements.txt",
                  ".\\README.md",
                  ".\\LICENSE",
                  ".\\CHANGELOG.md",
                  #!modules
                  ".\\modules\\",
                  ".\\modules\\FunctionLibs.py",
                  ".\\modules\\pic.png",
                  ".\\modules\\restart.py",
                  ".\\modules\\ncmtomusic\\",
                  ".\\modules\\ncmtomusic\\modules\\",
                  ".\\modules\\ncmtomusic\\modules\\Json_Function.py",
                  ".\\modules\\ncmtomusic\\modules\\mcntomusic.py",
                  ".\\modules\\ncmtomusic\\ncm1\\",
                  ".\\modules\\ncmtomusic\\ncm1\\mcntomusic.py",
                  ".\\modules\\ncmtomusic\\ncm1\\processing_list.json",
                  ".\\modules\\ncmtomusic\\ncm2\\",
                  ".\\modules\\ncmtomusic\\ncm2\\mcntomusic.py",
                  ".\\modules\\ncmtomusic\\ncm2\\processing_list.json",
                  ".\\modules\\ncmtomusic\\ncm3\\",
                  ".\\modules\\ncmtomusic\\ncm3\\mcntomusic.py",
                  ".\\modules\\ncmtomusic\\ncm3\\processing_list.json",
                  ".\\modules\\ncmtomusic\\ncm4\\",
                  ".\\modules\\ncmtomusic\\ncm4\\mcntomusic.py",
                  ".\\modules\\ncmtomusic\\ncm4\\processing_list.json",
                  ".\\modules\\ncmtomusic\\ncm5\\",
                  ".\\modules\\ncmtomusic\\ncm5\\mcntomusic.py",
                  ".\\modules\\ncmtomusic\\ncm5\\processing_list.json",
                  ".\\modules\\ncmtomusic\\global_allocation.py",
                  ".\\modules\\ncmtomusic\\global_set.json",
                  #!localizations
                  ".\\localizations",
                  ".\\localizations\\ZH_CN.json",  #你至少要个中文吧，我看什么语言文件都没你怎么运行
                  #!output
                  ".\\output",
                ]}
    list_not = []
    for i in dic["files"]:
        file_path = WorkSpace + i
        if os.path.exists(file_path):
            continue
        else:
            list_not.append(file_path)
    return list_not

if __name__ == "__main__":
    if Check_Files() == []:
        parser = argparse.ArgumentParser(description='Check Start 程序检查命令行')
        parser.add_argument('--debug',default="True")
        args = parser.parse_args()
        debugs = args.debug

        if debugs == "True":
            sys.path.append('')
            print(f"正在使用如下参数启动: {' '.join(sys.argv[1:])}")
            print("YEAH!!!!!!!!!!!!!!!")
            os.system("taskkill /f /im cmd.exe")
            os.system("start cmd /k python.exe -u main.py")
        else:
            sys.path.append('')
            print(f"正在使用如下参数启动: {' '.join(sys.argv[1:])}")
            print("YEAH!!!!!!!!!!!!!!!")
            os.system("taskkill /f /im cmd.exe")
            os.system("start cmd /k pythonw.exe -u main.py")
    else:
        erro_file=Check_Files()
        erro_file = str(erro_file)
        erro_file.replace("[","")
        erro_file.replace("]","")
        erro_file.replace("'","")
        error = erro_file+":无法找到文件错误，无法找到指定运行必须库，请检查文件完整性或重新下载！The file error could not be found, the specified run must library could not be found, please check file integrity or re-download!"
        tkinter.messagebox.showerror("Tool By QinQiuFox执行检测程序",error)
        os.system("taskkill /f /im cmd.exe")