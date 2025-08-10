#!/usr/bin/env python
# -*-coding:utf-8-*-
#!系统自带支持库
import tkinter
import tkinter.messagebox
import tkinter.ttk
from tkinter import ttk
import os
import sys
import subprocess
import threading
import time
from tkinter import scrolledtext
from PIL import Image, ImageTk
#!函数库（运行集合)
from modules.ncmtomusic import global_allocation
import move_files
from modules import FunctionLibs

class GUI:
    #窗口参数
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.title('Tool By QinQiuFox')
        self.root.geometry("500x500+350+200")
        self.root.resizable(False, False)
        self.root.iconphoto(True, tkinter.PhotoImage(file = '.\\modules\\pic.png'))
        self.canvas = tkinter.Canvas(self.root, width=500, height=600)
        self.canvas.place(x=0, y=0)
        self.bg_image = Image.open(".\\modules\\pic.png")
        self.bg_image = self.bg_image.resize((500, 600), Image.Resampling.LANCZOS)
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor="nw")
        self.style = ttk.Style(self.root)
        self.style.theme_use('clam')
        self.style.configure("TButton", padding=6, relief="flat", background="#007BFF", foreground="white", font=("Arial", 10, "bold"))
        self.style.map("TButton", background=[('active', '#0056b3')])
        self.style.configure("TLabel", background="#f4f4f4", font=("Arial", 10))
        self.style.configure("TEntry", fieldbackground="#ffffff", font=("Arial", 10))
        self.interface()

    #GUI
    def interface(self):
        FunctionLibs.infos()
        language_choice = FunctionLibs.json_read("UI-Config.json")
        language_choice_c = language_choice["language"]
        language_file_choice = language_choice_c + ".json"
        language_dic=FunctionLibs.json_read(".\\localizations\\" + language_file_choice)
        language=language_dic   #语言选择器

        print(language["使用python解释器位置："] + sys.executable)    #获取解释器目录（调试）

        global WorkSpace
        WorkSpace = sys.path[0] #获取运行目录

        print(language["加载根目录："], WorkSpace)
        print(language["加载配置文件目录："], WorkSpace+"\\UI-Config.json")
        FunctionLibs.json_write(WorkSpace + "\\UI-Config.json", "WorkSpace", WorkSpace)

        tab_main = tkinter.ttk.Notebook()   #创建分页
        tab_main.place(relx=0.02, rely=0.02, relwidth=0.887, relheight=0.876)

        def base64c_page():#Base64页面代码
            choice_file_B64=tkinter.Label(tabB64, text = language["选择输入文件路径："])
            choice_file_B64.place(x=5, y=5)

            def select_file_b64():  #选择文件
                global select_file_path_b64
                select_file_path_b64 = FunctionLibs.select_file()
                if os.path.exists(select_file_path_b64):
                    choice_file_B64_lb.config(state = "normal")
                    inputselectpath.set(select_file_path_b64)
                    choice_file_B64_lb.config(state = "disabled")
                    print(language["读取所有文件成功！"])
                    print(language["加载"] + select_file_path_b64 + language["成功！"])
                else:
                    tkinter.messagebox.showerror("Tool By QinQiuFox", language["本地文件不存在"])

            inputselectpath = tkinter.StringVar()   #创建容器
            choice_file_B64_lb=tkinter.Entry(tabB64, textvariable = inputselectpath)
            choice_file_B64_lb.place(x=5, y=35, width=300)
            choice_file_B64_bu=tkinter.Button(tabB64, text=language["选择单个文件"], command=select_file_b64)
            choice_file_B64_bu.place(x=5, y=65)

            input_file_name_lable = tkinter.Label(tabB64, text=language["设置要进行Base64码的文件名："])
            input_file_name_lable.place(x=5, y=95)
            input_file_name = tkinter.Entry(tabB64)
            input_file_name.place(x=5, y=125, width=300)

            choice_file_B64_lb.config(state = "disabled") #禁止随意编辑

            def run_base64(method): #运行
                Define_setting = FunctionLibs.json_read(WorkSpace + "\\UI-Config.json")
                Is_Base64_Show_State = Define_setting["B64ShowState"]
                if method == "encode":
                    if Is_Base64_Show_State == "1":
                        FunctionLibs.runencode_b(select_file_path_b64, input_file_name.get())
                        tkinter.messagebox.showinfo("Tool By QinQiuFox", language["执行成功"])
                        print(language["执行成功"])
                        move_files.move_file_obj()
                    elif Is_Base64_Show_State == "2":
                        return_value = FunctionLibs.runencodetostr(select_file_path_b64)
                        tkinter.messagebox.showinfo("Tool By QinQiuFox", language["执行成功"])
                        print(language["执行成功"])
                        Text_Box_down.config(state = "normal")
                        Text_Box_down.delete(0.0, tkinter.END)
                        Text_Box_down.insert(tkinter.END, str(return_value))
                        Text_Box_down.config(state = "disabled")
                    else:
                        tkinter.messagebox.showerror("Tool By QinQiuFox", "警告！配置文件异常，请检查数值！")
                elif method == "decode":
                    if Is_Base64_Show_State == "1":
                        FunctionLibs.rundecode_b(select_file_path_b64, input_file_name.get())
                        tkinter.messagebox.showinfo("Tool By QinQiuFox", language["执行成功"])
                        print(language["执行成功"])
                        move_files.move_file_xpp()
                    elif Is_Base64_Show_State == "2":
                        return_value = FunctionLibs.rundecodetostr(select_file_path_b64)
                        tkinter.messagebox.showinfo("Tool By QinQiuFox", language["执行成功"])
                        print(language["执行成功"])
                        Text_Box_down.config(state = "normal")
                        Text_Box_down.delete(0.0, tkinter.END)
                        Text_Box_down.insert(tkinter.END, str(return_value))
                        Text_Box_down.config(state = "disabled")
                    else:
                        tkinter.messagebox.showerror("Tool By QinQiuFox", "警告！配置文件异常，请检查数值！")
                else:
                    tkinter.messagebox.showerror("Tool By QinQiuFox", "未知错误")

            def start_run_base64(method_a): #创建多线程
                bs64_start_time = time.time()
                T_base64 = threading.Thread(target = run_base64(method_a))
                T_base64.daemon=True
                T_base64.start()
                bs64_end_time = time.time()
                print("执行时间：{}秒".format(bs64_end_time - bs64_start_time))

            def if_ckick_encode():
                start_run_base64("encode")

            def if_click_decode():
                start_run_base64("decode")

            def if_click_clear():
                Text_Box_down.config(state = "normal")
                Text_Box_down.delete(0.0, tkinter.END)
                Text_Box_down.config(state = "disabled")

            Butt_encode = tkinter.Button(tabB64, text=language["编码"], command=if_ckick_encode)
            Butt_encode.place(x=5, y=170)

            Butt_decode = tkinter.Button(tabB64, text=language["解码"], command=if_click_decode)
            Butt_decode.place(x=60, y=170)

            Butt_clear = tkinter.Button(tabB64, text="清屏", command=if_click_clear)
            Butt_clear.place(x=115, y=170)

            Text_Box_down = scrolledtext.ScrolledText(tabB64, wrap=tkinter.WORD,font="15")
            Text_Box_down.place(x=5, y=220, width=450, height=240)
            Text_Box_down.config(state = "disabled")



        def haxic_page():   #哈希编码页面
            choice_file_haxi=tkinter.Label(tabhaxi, text=language["选择输入文件路径："])
            choice_file_haxi.place(x=5, y=5)

            def select_file():  #选择文件
                global select_file_path_haxi
                select_file_path_haxi = FunctionLibs.select_file()
                choice_file_haxi_lb.config(state = "normal")
                inputselectpath.set(select_file_path_haxi)
                choice_file_haxi_lb.config(state = "disabled")
                if os.path.exists(select_file_path_haxi):
                    print(language["读取所有文件成功！"])
                    print(language["加载"] + select_file_path_haxi + language["成功！"])
                else:
                    tkinter.messagebox.showerror("Tool By QinQiuFox", language["本地文件不存在"])

            inputselectpath = tkinter.StringVar()
            choice_file_haxi_lb=tkinter.Entry(tabhaxi, textvariable = inputselectpath)
            choice_file_haxi_lb.place(x=5, y=35, width=300)
            choice_file_haxi_bu=tkinter.Button(tabhaxi, text=language["选择单个文件"], command=select_file)
            choice_file_haxi_bu.place(x=5, y=65)

            choice_file_haxi_lb.config(state = "disabled")

            input_file_name_lable = tkinter.Label(tabhaxi, text=language["设置要进行哈希编码的文件名："])
            input_file_name_lable.place(x=5, y=95)
            input_file_name = tkinter.Entry(tabhaxi)
            input_file_name.place(x=5, y=125, width=300)

            input_haxi_method_label = tkinter.Label(tabhaxi, text=language["设置哈希计算方法："])
            input_haxi_method_label.place(x=5, y=155)
            input_haxi_method = tkinter.ttk.Combobox(tabhaxi, values=["sha1","sha256","md5"], state="readonly")
            input_haxi_method.place(x=5, y=185, width=300)
            input_haxi_method.set("")

            input_haxi_salt_label = tkinter.Label(tabhaxi, text=language["设置哈希算法盐位数："])
            input_haxi_salt_label.place(x=5,y=215)
            input_haxi_salt = tkinter.ttk.Combobox(tabhaxi, values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"], state="readonly")
            input_haxi_salt.place(x=5, y=245, width=300)
            input_haxi_salt.set("")

            def run_haxi():
                haxi_start_time = time.time()
                FunctionLibs.runencode_h(select_file_path_haxi,input_haxi_method.get(), input_haxi_salt.get(), input_file_name.get())
                print(language["执行成功"])
                tkinter.messagebox.showinfo("Tool By QinQiuFox", language["执行成功"])
                move_files.move_file_obj()
                haxi_end_time = time.time()
                print("执行时间：{}秒".format(haxi_end_time - haxi_start_time))

            def start_run_haxi():
                T_haxi = threading.Thread(target = run_haxi)
                T_haxi.daemon=True
                T_haxi.start()

            shart_haxi = tkinter.Button(tabhaxi, text=language["运行"], command=start_run_haxi)
            shart_haxi.place(x=5, y=300)

        def ncmtomusic():   #网易云格式转换页面
            choice_file_ncm=tkinter.Label(tabncm, text = language["选择输入文件夹路径："])
            choice_file_ncm.place(x=5, y=5)

            def select_folder():    #选择文件夹
                global selected_folder_ncm
                selected_folder_ncm = FunctionLibs.select_folder()
                choice_file_ncm_lb.config(state = "normal")
                inputselectpath_ncm.set(selected_folder_ncm)
                choice_file_ncm_lb.config(state = "disabled")
                print(language["加载"]+selected_folder_ncm+language["成功！"])
                FunctionLibs.json_write("UI-Config.json", "ncmpath", str(selected_folder_ncm))

            inputselectpath_ncm = tkinter.StringVar()
            choice_file_ncm_lb=tkinter.Entry(tabncm, textvariable = inputselectpath_ncm)
            choice_file_ncm_lb.place(x=5, y=35, width=300)
            choice_file_ncm_bu=tkinter.Button(tabncm, text=language["选择单个文件夹"], command=select_folder)
            choice_file_ncm_bu.place(x=5, y=65)
            ncm_auto_path = FunctionLibs.json_read("UI-Config.json")
            ncm_auto_path = ncm_auto_path["ncmpath"]
            inputselectpath_ncm.set(ncm_auto_path)

            choice_file_ncm_lb.config(state = "disabled")

            def run_ncm():
                ncm_start_time = time.time()
                global_allocation.run_main(choice_file_ncm_lb.get())
                print(language["执行成功"])
                ncm_end_time = time.time()
                print("执行时间：{}秒".format(ncm_end_time - ncm_start_time))

            def start_run_ncm():
                T_ncm = threading.Thread(target = run_ncm)
                T_ncm.daemon=True
                T_ncm.start()

            shart_ncm = tkinter.Button(tabncm, text=language["运行"], command=start_run_ncm)
            shart_ncm.place(x=5, y=100)

        def setting_page(): #!设置页面

            #!'''设置输出目录部分设置'''
            Define_setting = FunctionLibs.json_read(WorkSpace + "\\UI-Config.json")
            save_path_label = tkinter.Label(tabs, text=language["设置输出目录："])
            save_path_label.place(x=5, y=5)
            save_path_input = tkinter.Entry(tabs)
            save_path_input.place(x=5, y=35, width=300)

            save_path_input.config(state = "normal")
            save_path_input.delete(0, tkinter.END)
            save_path_input.insert(0, Define_setting["OutPutPath"])
            save_path_input.config(state = "disabled")

            def save_path():
                path_save = FunctionLibs.select_folder()
                FunctionLibs.json_write(".\\UI-Config.json", "OutPutPath", str(path_save))
                save_path_input.config(state = "normal")
                save_path_input.delete(0, tkinter.END)
                save_path_input.insert(0, str(path_save))
                save_path_input.config(state = "disabled")
                print("已经设置输出目录为：{}".format(path_save))
            save_path_button = tkinter.Button(tabs, text=language["选择"], command=save_path)
            save_path_button.place(x=5, y=55)

            #!'''设置页面语言部分'''
            choice_language = tkinter.Label(tabs, text=language["可选页面语言："])
            choice_language.place(x=5, y=90)
            choice_language_list = tkinter.Entry(tabs)
            choice_language_list.place(x=5, y=115, width=400)
            language_list_list = FunctionLibs.scan_run(WorkSpace + ".\\localizations")
            language_list=str(language_list_list)
            language_list=language_list.replace("[", "")
            language_list=language_list.replace("]", "")
            language_list=language_list.replace("'", "")
            language_list=language_list.replace(".json", "")
            choice_language_list.config(state = "normal")
            choice_language_list.insert(0, language_list)
            choice_language_list.config(state = "readonly")

            language_now_la = tkinter.Label(tabs, text = language["当前语言："])
            language_now_la.place(x=5, y=145)
            language_now = tkinter.Label(tabs, text = str(language_choice_c))
            language_now.place(x=60, y=145)

            choice_language_input_label = tkinter.Label(tabs, text = language["输入选择的语言文件："])
            choice_language_input_label.place(x=5, y=165)

            def selected(event):
                language_file_name=str(combo_clanguage.get())
                language_name = language_file_name.replace(".json","")
                FunctionLibs.json_write("UI-Config.json", "language", language_name)
                print(language["页面语言选择--->"], combo_clanguage.get())

            combo_clanguage = tkinter.ttk.Combobox(tabs, values=language_list_list, state="readonly")
            combo_clanguage.current(0)
            combo_clanguage.bind('<<ComboboxSelected>>', selected)
            combo_clanguage.place(x=5, y=185, width=300)
            combo_clanguage.set(str(language_choice_c))

            def save_language_set():
                tkinter.messagebox.showinfo("Tool By QinQiuFox", language["设置完成后，即将自动重启！"])
                subprocess.Popen(['python', ".\\modules\\restart.py"])
                exit()

            language_save = tkinter.Button(tabs, text=language["应用设置语言"], command=save_language_set)
            language_save.place(x=5, y=210)

            #!'''设置NCM处理进程数设置'''
            def core(event):
                ncm_core_number = str(combo_ncm_core.get())
                FunctionLibs.json_write(WorkSpace + ".\\modules\\ncmtomusic\\global_set.json", "core_num", int(ncm_core_number))
                print(language["ncm处理进程数选择--->"], combo_ncm_core.get())

            ncm_auto_core = FunctionLibs.json_read(WorkSpace + ".\\modules\\ncmtomusic\\global_set.json")
            ncm_auto_core_num = ncm_auto_core["core_num"]
            core_num = int(ncm_auto_core_num)
            ncm_core_num = tkinter.Label(tabs, text = language["设置ncm处理进程数："])
            ncm_core_num.place(x=5, y=245)

            combo_ncm_core = tkinter.ttk.Combobox(tabs, values=["1", "2", "3", "4", "5"], state="readonly")
            combo_ncm_core.current(0)
            combo_ncm_core.bind('<<ComboboxSelected>>', core)
            combo_ncm_core.place(x=5, y=265, width=300)
            combo_ncm_core.set(str(core_num))

            #!'''设置Base64输出状态'''
            def core_set_bs64(event=None):
                bs64_state = str(combo_set_bs64.get())
                if bs64_state == "输出至文件":
                    FunctionLibs.json_write(WorkSpace + ".\\UI-Config.json", "B64ShowState", "1")
                    print("Base64输出状态--->", combo_set_bs64.get())
                elif bs64_state == "输出至窗口":
                    FunctionLibs.json_write(WorkSpace + ".\\UI-Config.json", "B64ShowState", "2")
                    print("Base64输出状态--->", combo_set_bs64.get())
                else:
                    pass

            set_bs64_state = tkinter.Label(tabs, text="设置Base64输出状态:")
            set_bs64_state.place(x=5, y=300)

            combo_set_bs64 = tkinter.ttk.Combobox(tabs, values=["输出至文件","输出至窗口"], state="readonly")
            combo_set_bs64.current(0)
            combo_set_bs64.bind('<<ComboboxSelected>>', core_set_bs64)
            combo_set_bs64.place(x=5, y=320, width=300)
            Define_setting = FunctionLibs.json_read(WorkSpace + "\\UI-Config.json")
            Is_Base64_Show_State = Define_setting["B64ShowState"]
            if Is_Base64_Show_State == "1":
                combo_set_bs64.set(str("输出至文件"))
            elif Is_Base64_Show_State == "2":
                combo_set_bs64.set(str("输出至窗口"))
            else:
                pass

        #页面应用
        '''Base64编码'''
        tabB64=tkinter.Frame(tab_main)
        tabB64.place(x=0, y=30)
        tab_main.add(tabB64, text = "Base64")

        base64c_page()

        '''哈希编码'''
        tabhaxi=tkinter.Frame(tab_main)
        tabhaxi.place(x=0, y=60)
        tab_main.add(tabhaxi, text = language["哈希"])

        haxic_page()

        '''ncm转格式'''
        tabncm=tkinter.Frame(tab_main)
        tabncm.place(x=0, y=90)
        tab_main.add(tabncm, text = language["NCM工具"])

        ncmtomusic()

        '''设置'''
        tabs=tkinter.Frame(tab_main)
        tabs.place(x=0, y=120)
        tab_main.add(tabs, text = language["设置"])

        setting_page()

if __name__ == '__main__':
        sys_start_time = time.time()
        print("环境检查完成，正在启动！")
        FunctionLibs.show_error()
        a = GUI()
        sys_end_time = time.time()
        print("程序启动时间：{}s".format(sys_end_time - sys_start_time))
        a.root.mainloop()
        print("进程已退出！")
        exit()