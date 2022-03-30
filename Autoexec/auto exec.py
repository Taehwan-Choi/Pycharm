import tkinter as tk
import psutil
import os
import time
import csv
import threading
import sys


pause=False


def check_program():
    global pause
    while True: 
        if pause == True:
            return
        flaga=False
        flagb=False
        for k in psutil.process_iter():
            if k.name() == "TagData.exe" and k.status()=='running':
                flaga=True
            
            if k.name() == "TagDataProcess.exe" and k.status() =='running':
                flagb=True
    
        if flaga==False:
            try : 
                os.startfile(path1)
                f=open("auto exec log.txt", "a")
                print(time.ctime(), f"{path1}가 재실행 되었습니다.", file=f)
                f.close()
            except: 
                f=open("auto exec log.txt", "a")
                print(time.ctime(), "오류 발생", file=f)
                f.close()
        if flagb==False:
            try :
                os.startfile(path2)
                f=open("auto exec log.txt", "a")
                print(time.ctime(), f"{path2}가 재실행 되었습니다.", file=f)
                f.close()
            except: 
                f=open("auto exec log.txt", "a")
                print(time.ctime(), "오류 발생", file=f)
                f.close()
            
        time.sleep(10)
    

def th():
    th = threading.Thread(target=check_program)
    th.daemon=True
    th.start()


pathlist=[]


f=open("path_env.csv",'r')
path=csv.reader(f)


for k in path:
    pathlist.append(k)
    
path1=pathlist[0][0]
path2=pathlist[1][0]


root=tk.Tk()
root.title("프로그램 실행 감시")
label1=tk.Label(root,text='TagData : ')
label1.grid(row=0, column=0)
label1_1=tk.Label(root, text=path1)
label1_1.grid(row=0, column=1)


label2=tk.Label(root,text='TagDataProcess : ')
label2.grid(row=1, column=0)

label2_2=tk.Label(root, text=path2)
label2_2.grid(row=1, column=1)


def button_action():
    check_program()
    
        
def button_action2():
    global pause
    pause = True
    root.destroy()
    sys.exit()
    
    
button1=tk.Button(root, text='실행', command=th)
button1.grid(row=2,column=0)
button2=tk.Button(root, text='실행 감시 중지&종료', command=button_action2)
button2.grid(row=2,column=1)


explain=tk.Label(root,text='(프로그램 종료시 10초마다 자동으로 실행)')
explain.grid(row=3,column=1)


root.mainloop()

    

    
