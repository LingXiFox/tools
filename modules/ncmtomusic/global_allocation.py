from modules import FunctionLibs
import sys
import subprocess
import tkinter.messagebox
import modules.ncmtomusic.modules.mcntomusic as mcntomusic
import os
from tqdm import tqdm

#define
WorkSpace = sys.path[0]
ncm1_path = WorkSpace+"\\modules\\ncmtomusic\\ncm1\\mcntomusic.py"
ncm2_path = WorkSpace+"\\modules\\ncmtomusic\\ncm2\\mcntomusic.py"
ncm3_path = WorkSpace+"\\modules\\ncmtomusic\\ncm3\\mcntomusic.py"
ncm4_path = WorkSpace+"\\modules\\ncmtomusic\\ncm4\\mcntomusic.py"
ncm5_path = WorkSpace+"\\modules\\ncmtomusic\\ncm5\\mcntomusic.py"

#文件夹计数（不包含子文件夹）
def list_files_in_directory(directory):
    list_totle=[]
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            list_totle.append(file_path)
    count=len(list_totle)
    return count

def file_extension(path):
    return os.path.splitext(path)[1]

def scan_run(file_path:str):
    list_global = []
    list = os.listdir(file_path)
    for i in tqdm(range(0,len(list)),desc="扫描进度"):
        path = os.path.join(file_path, list[i])
        if os.path.isfile(path):
            if os.path.isfile(path):
                if file_extension(path) == ".ncm":
                    try:
                        list_global.append(path)
                    except:
                        pass
    return list_global

def run_main(path:str):
    list_main_global = list(scan_run(path))
    core_num_json = FunctionLibs.json_read(WorkSpace+".\\modules\\ncmtomusic\\global_set.json")
    core_num = int(core_num_json["core_num"])

    #count
    count = 0

    #function
    count = len(list_main_global)
    if count == 0:
        tkinter.messagebox.showinfo("Error", "No files to process")
    elif count < 5:
        mcntomusic.run(list_main_global)
        tkinter.messagebox.showinfo("Info", "All files processed")
    elif count >= 5:
        if core_num == 1:
            #!1
            mcntomusic.run(list_main_global)
            tkinter.messagebox.showinfo("Info", "All files processed")
        elif core_num == 2:
            #!2
            list_length = count
            list_per = int(list_length / 2)
            total_per = list_per * 2
            if total_per < list_length:
                ncm1=list_per
                ncm2=list_per+(list_length-total_per)
            elif total_per == list_length:
                ncm1=list_per
                ncm2=list_per
            else:
                pass
            ncm1_list = list_main_global[:ncm1]
            del list_main_global[:ncm1]
            ncm2_list = list_main_global[:ncm2]
            del list_main_global[:ncm2]
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm1\\processing_list.json", "abc", ncm1_list)
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm2\\processing_list.json", "abc", ncm2_list)
            subprocess.Popen(['python.exe', ncm1_path])
            subprocess.Popen(['python.exe', ncm2_path])
        elif core_num == 3:
            #!3
            list_length = count
            list_per = int(list_length / 3)
            total_per = list_per * 3
            if total_per < list_length:
                ncm1=list_per
                ncm2=list_per
                ncm3=list_per+(list_length-total_per)
            elif total_per == list_length:
                ncm1=list_per
                ncm2=list_per
                ncm3=list_per
            else:
                pass
            ncm1_list = list_main_global[:ncm1]
            del list_main_global[:ncm1]
            ncm2_list = list_main_global[:ncm2]
            del list_main_global[:ncm2]
            ncm3_list = list_main_global[:ncm3]
            del list_main_global[:ncm3]
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm1\\processing_list.json", "abc", ncm1_list)
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm2\\processing_list.json", "abc", ncm2_list)
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm3\\processing_list.json", "abc", ncm3_list)
            subprocess.Popen(['python.exe', ncm1_path])
            subprocess.Popen(['python.exe', ncm2_path])
            subprocess.Popen(['python.exe', ncm3_path])
        elif core_num == 4:
            #!4
            list_length = count
            list_per = int(list_length / 4)
            total_per = list_per * 4
            if total_per < list_length:
                ncm1=list_per
                ncm2=list_per
                ncm3=list_per
                ncm4=list_per+(list_length-total_per)
            elif total_per == list_length:
                ncm1=list_per
                ncm2=list_per
                ncm3=list_per
                ncm4=list_per
            else:
                pass
            ncm1_list = list_main_global[:ncm1]
            del list_main_global[:ncm1]
            ncm2_list = list_main_global[:ncm2]
            del list_main_global[:ncm2]
            ncm3_list = list_main_global[:ncm3]
            del list_main_global[:ncm3]
            ncm4_list = list_main_global[:ncm4]
            del list_main_global[:ncm4]
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm1\\processing_list.json", "abc", ncm1_list)
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm2\\processing_list.json", "abc", ncm2_list)
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm3\\processing_list.json", "abc", ncm3_list)
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm4\\processing_list.json", "abc", ncm4_list)
            subprocess.Popen(['python.exe', ncm1_path])
            subprocess.Popen(['python.exe', ncm2_path])
            subprocess.Popen(['python.exe', ncm3_path])
            subprocess.Popen(['python.exe', ncm4_path])
        elif core_num == 5:
            #!5
            list_length = count
            list_per = int(list_length / 5)
            total_per = list_per * 5
            if total_per < list_length:
                ncm1=list_per
                ncm2=list_per
                ncm3=list_per
                ncm4=list_per
                ncm5=list_per+(list_length-total_per)
            elif total_per == list_length:
                ncm1=list_per
                ncm2=list_per
                ncm3=list_per
                ncm4=list_per
                ncm5=list_per
            else:
                pass
            ncm1_list = list_main_global[:ncm1]
            del list_main_global[:ncm1]
            ncm2_list = list_main_global[:ncm2]
            del list_main_global[:ncm2]
            ncm3_list = list_main_global[:ncm3]
            del list_main_global[:ncm3]
            ncm4_list = list_main_global[:ncm4]
            del list_main_global[:ncm4]
            ncm5_list = list_main_global[:ncm5]
            del list_main_global[:ncm5]
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm1\\processing_list.json", "abc", ncm1_list)
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm2\\processing_list.json", "abc", ncm2_list)
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm3\\processing_list.json", "abc", ncm3_list)
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm4\\processing_list.json", "abc", ncm4_list)
            FunctionLibs.json_write(WorkSpace+".\\modules\\ncmtomusic\\ncm5\\processing_list.json", "abc", ncm5_list)
            subprocess.Popen(['python.exe', ncm1_path])
            subprocess.Popen(['python.exe', ncm2_path])
            subprocess.Popen(['python.exe', ncm3_path])
            subprocess.Popen(['python.exe', ncm4_path])
            subprocess.Popen(['python.exe', ncm5_path])
    else:
        tkinter.messagebox.showinfo("Error", "Something went wrong")
        sys.exit()