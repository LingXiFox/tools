#*-适用于所有的函数库*#

#*base64c.py*#
import base64

def scan_file_line_to_list(file_path)->list:
    filename = file_path
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

def is_base64(s):
    try:
        base64.b64decode(s)
        return True
    except ValueError:
        return False


def runencode_b(path,name):
    try:
        print("\n")
        name1 = name + ".xppOBJ"
        f = open(path,"rb")
        file = open(name1,"w")
        line = f.readline()
        while line:
            line = f.readline()
            encode = base64.b64encode(line)
            print("Write Code Massage in" + "  " +name1+"------>",end='')
            print(encode)
            encode1 = str(encode)
            encode1 = encode1.replace("b'","")
            encode1 = encode1.replace("'","")
            encode1 = encode1.replace(" ","")
            file.write(encode1)
            file.write("\n")
        f.close()
    except:
        print("编码失败，出现意外错误!")

def rundecode_b(path,name):
    try:
        print("\n")
        name1 = name + ".xpp"
        f = open(path,"rb")
        file = open(name1,"w")
        line = f.readline()
        while line:
            line = f.readline()
            encode = base64.b64decode(line)
            print("Unlock Code Massage in" + "  " +name1+"------>",end='')
            print(encode)
            encode1 = str(encode)
            encode1 = encode1.replace("b'","")
            encode1 = encode1.replace("'","")
            encode1 = encode1.replace(" ","")
            encode = encode1.replace("\r\n","")
            file.write(encode1)
            file.write("\n")
        f.close()
    except:
        print("编码失败，出现意外错误!")

def runencodetostr(input:str)->str:
    input = input.encode("utf-8")
    file_in_list = scan_file_line_to_list(input)
    return_list = []
    pgik = ''
    for i in file_in_list:
        encode = base64.b64encode(i.encode('utf-8'))
        encode1 = str(encode)
        encode1 = encode1.replace("b'","")
        encode1 = encode1.replace("'","")
        encode1 = encode1.replace(" ","")
        return_list.append(encode1)
    for j in return_list:
        pgik = pgik +j + "\n"
    return pgik

def rundecodetostr(input:str)->str:
    input = input.encode("utf-8")
    file_in_list = scan_file_line_to_list(input)
    return_list = []
    pgik = ''
    for i in file_in_list:
        encode = base64.b64decode(i.encode('utf-8'))
        encode1 = str(encode)
        encode1 = encode1.replace("b'","")
        encode1 = encode1.replace("'","")
        encode1 = encode1.replace(" ","")
        return_list.append(encode1)
    for j in return_list:
        pgik = pgik +j + "\n"
    return pgik

#*count_file.py*#
def count_file_line(path):

    count = len(open(path,'r').readlines())
    count = int(count)
    return count

def count_file_world(path):

    count = len(open(path,'r').read())
    count = int(count)
    return count

#*haxi.py*#
from tqdm import *
import werkzeug.security

def HaXi(password,method,salt)->str:

    method_user_input ="pbkdf2:"+method
    saltL_user_input = int(salt)

    result = werkzeug.security.generate_password_hash(password,method=method_user_input,salt_length=saltL_user_input)
    return result


def runencode_h(path,hethod,salt,name):
    num = 0
    count = len(open(path,'r').readlines())
    print("\n")
    name1 = name + ".xppOBJ"
    f = open(path,"rb")
    file = open(name1,"w")
    line = f.readline()
    while line:
        line = f.readline()
        line = str(line)
        encode = HaXi(line,hethod,salt)
        print("Write Code Massage in" + "  " +name1+"------>",end='')
        print(encode)
        num = num+1
        encode1 = str(encode)
        file.write(encode1)
        file.write("\n")
        if num == count:
            f.close()
            break

#*Json_Function.py*#
import json

def json_read(json_path):

    with open(json_path,'r',encoding='utf8')as fp:

        json_data = json.load(fp)

    return json_data

def json_write(path:str,key:str,value:str):

    key = str(key)

    path = str(path)

    def get_json_data():
        with open(path, 'rb') as f:
            params = json.load(f)
            params[key] = value
            print("写入配置文件信息：", params)
        return params

    def write_json_data(params):
        with open(path, 'w') as r:
            json.dump(params, r)

    the_revised_dict = get_json_data()
    write_json_data(the_revised_dict)

#*ncmtomusic_start.py*#
import os
from tqdm import tqdm
import sys
import subprocess
import json

def json_write(path:str,key:str,value:str):
    key = str(key)
    path = str(path)
    def get_json_data():
        with open(path, 'rb') as f:
            params = json.load(f)
            params[key] = value
            print("写入配置文件信息：", params)
        return params
    def write_json_data(params):
        with open(path, 'w') as r:
            json.dump(params, r)
    the_revised_dict = get_json_data()
    write_json_data(the_revised_dict)

WorkSpace = sys.path[0]

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

def run(path:str):
    json_write(WorkSpace+".\\modules\\ncmtomusic\\global_list.json","list_global",list(scan_run(path)))
    path= WorkSpace+".\\modules\\ncmtomusic\\global_allocation.py"
    subprocess.Popen(['python.exe', path])

#*scan_path.py*#
import os

def scan_run(rootpath:str)->list:
    root = rootpath
    for dirpath, dirnames, filenames in os.walk(root):
        return filenames

def scan_file_line_to_list(file_path)->list:
    filename = file_path
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

#*select_function.py*#
from tkinter import filedialog

def select_folder()->str:
    # 文件夹选择
    selected_folder = filedialog.askdirectory()
    return selected_folder

def select_file()->str:
    #单个文件选择
    global select_file_path
    select_file_path = filedialog.askopenfilename(filetypes=[("Support Files",".xpp .zzh .txt .xppOBJ")])
    return select_file_path

def select_files()->tuple:
    # 多个文件选择
    selected_files_path = filedialog.askopenfilenames()
    return selected_files_path

#*showinfo.py*#
import os
def info():
    print("你的运行环境为：")
    os.system("python --version")
    print("程序编写环境为：")
    print("Python 3.13.2")

    print("####################################")
    print("#                                  #")
    print("#      泠溪小狐狸编写，侵权必究    #")
    print("#                                  #")
    print("####################################")


def infos():
    info()
    print("\n#########################日志#########################")

#*显示警告*#
show_error_list = [
    "清屏二字暂时不支持外语请见谅"
]
def show_error():
    for i in show_error_list:
        print("警告："+ i + "\n")