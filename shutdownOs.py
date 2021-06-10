# coding: utf-8

import subprocess
import sys

#from tkinter import messagebox


def shutdown(args):
  subprocess.call("shutdown /s /t 3 /f /d p:4:1", shell=True)


  # メッセージボックス（情報） 
  #messagebox.showinfo('確認', "取得温度" + str(temp))



  file = open("C:/Users/arata/Desktop/0402/ShutdownValue.txt", "w", encoding = "utf_8")
  file.writelines(args[1] + "\n")
  file.writelines(args[2] + "\n")


#shutdownOS(sys.argv)