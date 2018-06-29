#!/usr/bin/python3
from tkinter import *
import subprocess
from threading import Thread
from tkinter import messagebox
import re

# При старте гасить порты
check = subprocess.check_output('ps ax | grep 5900 |grep -v grep|awk \'{print $1}\'',shell=True)
proc = str(check)
proc = proc.replace('\'','')
proc = proc.replace('b','')
res = proc.split('\\n')
res = res[:-1]
res = [int(x) for x in res]
if res:
    try:
        for i in res:
              subprocess.call('kill -9 ' + str(i),shell=True)
    except subprocess.CalledProcessError:
              print('BAD')

root = Tk()
root.title('VNC')
root.geometry('300x200')
root.resizable(False, False)

def mes():
    messagebox.showinfo('info','Вы можете подключиться по vnc 2мя способами:\n1.Ввести номер хоста\n2.Ввести ip(имя) полностью\nПо умолчанию тунель пробрасывается на\nlocalhost:5900\nПри подключении можно указать порт самостоятельно')

butmes = Button(root,text='info',command=mes)
butmes.place(x = 130, y = 10)

inpv = Entry(width=3)                             # Ввод для Var1
inpv.place(x = 100, y = 52)
Label(root, text = 'номер\nхоста').place(x = 5, y = 45)
Label(root, text = 'host').place(x = 60, y = 52) # перед var1

inp = Entry(width=14)          # Ввод для Var2
inp.place(x = 15, y = 110)
Label(root, text = 'IP или имя хоста').place(x = 20, y=90)

port = Entry(width=5)          # port 
port.place(x = 90, y = 170)
Label(root, text = 'порт').place(x = 50, y=170)
Label(root, text = '(по необходимости)').place(x = 170, y = 170)

def var1():
    def c():
            p = port.get()
            q = inpv.get()
            if len(p) == 0:
                     try:
                          subprocess.call('ssh -o StrictHostKeyChecking=no -fN -L 5900:localhost:5900 host' + q,shell=True)
                          subprocess.call('vncviewer -passwordfile /home/.vnc/passwd localhost ',shell=True)
                          check = subprocess.check_output('ps ax | grep 5900 |grep -v grep|awk \'{print $1}\'',shell=True)
                          proc = str(check)
                          proc = proc.replace('\'','')
                          proc = proc.replace('b','')
                          res = proc.split('\\n')
                          res = res[:-1]
                          res = [int(x) for x in res]
                     finally:
                            if res:
                                 res = res[0]  
                                 try:
                                       subprocess.call('kill -9 ' + str(res),shell=True)
                                 except subprocess.CalledProcessError:
                                        print('BAD')
            else:
                     try:
                          subprocess.call('ssh -o StrictHostKeyChecking=no -fN -L '+p+':localhost:5900 host' + q,shell=True)
                          subprocess.call('vncviewer -passwordfile /home/.vnc/passwd localhost:'+p,shell=True)
                          check = subprocess.check_output('ps ax | grep '+p+' |grep -v grep|awk \'{print $1}\'',shell=True)
                          proc = str(check)
                          proc = proc.replace('\'','')
                          proc = proc.replace('b','')
                          res = proc.split('\\n')
                          res = res[:-1]  
                          res = [int(x) for x in res]
                     finally:
                            if res:
                                  res = res[0]  
                                  try:
                                          subprocess.call('kill -9 ' + str(res),shell=True)
                                  except subprocess.CalledProcessError:
                                            print('BAD')
    Thread(target=c).start()


def ping():
     q = 'host '+inpv.get()    #number
     try:
         a = subprocess.check_output('ping -c 1 ' + q, shell=True)
         print('OK')
         l['text'] = 'OK'
         l['bg'] = 'green'
     except subprocess.CalledProcessError:
         print('BAD')
         l['text'] = 'BAD'
         l['bg'] = 'red'

buttonping = Button(root, text='ping', command=ping)
buttonping.place(x = 250, y = 40)


l = Label(width=3)   # for ping 1
l.place(x=270, y=20)

def var2():
   def c():
       p = port.get()
       w = inp.get()
       if len(p) == 0:    
                     try:
                          subprocess.call('ssh -o StrictHostKeyChecking=no -fN -L 5900:localhost:5900 ' + w,shell=True)
                          subprocess.call('vncviewer -passwordfile /home/.vnc/passwd localhost ',shell=True)
                          check = subprocess.check_output('ps ax | grep 5900 |grep -v grep|awk \'{print $1}\'',shell=True)
                          proc = str(check)
                          proc = proc.replace('\'','')
                          proc = proc.replace('b','')
                          res = proc.split('\\n')
                          res = res[:-1]  
                          res = [int(x) for x in res]
                     finally:
                            if res:
                                   res = res[0]
                                   try: 
                                           subprocess.call('kill -9 ' + str(res),shell=True)
                                   except subprocess.CalledProcessError:
                                           print('BAD')
       else:
                     try:
                          subprocess.call('ssh -o StrictHostKeyChecking=no -fN -L '+p+':localhost:5900 ' + w,shell=True)
                          subprocess.call('vncviewer -passwordfile /home/.vnc/passwd localhost:'+p,shell=True)
                          check = subprocess.check_output('ps ax | grep '+p+' |grep -v grep|awk \'{print $1}\'',shell=True)
                          proc = str(check)
                          proc = proc.replace('\'','')
                          proc = proc.replace('b','')
                          res = proc.split('\\n')
                          res = res[:-1] 
                          res = [int(x) for x in res] 
                     finally:
                            if res:
                                  res = res[0]
                                  try:
                                           subprocess.call('kill -9 ' + str(res),shell=True)
                                  except subprocess.CalledProcessError:
                                           print('BAD')


   Thread(target=c).start()

def ping2():
     w = inp.get()
     try:
         a = subprocess.check_output('ping -c 1 ' + w, shell=True)
         print('OK')
         l2['text'] = 'OK'
         l2['bg'] = 'green'
     except subprocess.CalledProcessError:
         print('BAD')
         l2['text'] = 'BAD'
         l2['bg'] = 'red'

button = Button(root, text='Connect',command=var1)
button.place(x = 180, y = 40, height=35, width=59)

l2 = Label(width=3)  # for ping2
l2.place(x=270, y=85)

button2 = Button(root, text='Connect',command=var2)
button2.place(x = 180, y = 103, height=35, width=59)

buttonping2 = Button(root, text='ping', command=ping2)
buttonping2.place(x = 250, y = 107)
root.mainloop()