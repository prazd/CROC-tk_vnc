from tkinter import *
import subprocess
from threading import Thread
from tkinter import messagebox
import re

root = Tk()
q = Frame()

root.title('VNC')
root.geometry('300x200')
#Label(root, text = 'VAR1').pack()
inp = Entry(width=15)   # Ввод для Var2
alt = [1]
inpv = Entry(width=3)   # Ввод для Var1
inpv.place(x = 140, y = 20)

Label(root, text = 'ws-alt').place(x = 100, y=20)
#opt = OptionMenu(root,sv,*alt)
#opt.place(x = 50, y = 10)
#sv = StringVar(root)

def var1():
    def c():
       try:
            q = inpv.get()
            subprocess.call('ssh -fN -L 5900:localhost:5900 ws-alt-' + q,shell=True)
            subprocess.call('vncviewer localhost',shell=True)
       finally:
             try:
                  q = subprocess.check_output('ps ax | grep 5900 |grep -v grep|awk \'{print $1}\'',shell=True)
                  r = str(q)
                  r = r[2:-3]
                  if int(r):
                          subprocess.call('kill -9 ' + r,shell=True)
             except subprocess.CalledProcessError:
                          print('BAD')
    Thread(target=c).start()


def ping():
     q = 'name_of_host'+inpv.get()#number
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
buttonping.place(x = 250, y = 25)


l = Label(width=3)
l.place(x=270, y=5)

#Label(root, text = '').pack()
#Label(root, text = 'VAR2').pack()

#Label(root, text='ws-alt').place(x=10,y=90)
inp.place(x = 50, y = 90)

def var2():
   def c():
    try:
       global alt
       alt+=inp.get()
       w = inp.get()
       subprocess.call('ssh -fN -L 5900:localhost:5900 ' + w,shell=True)
       subprocess.call('vncviewer localhost',shell=True)
    finally:
        try:
             q = subprocess.check_output('ps ax | grep 5900 |grep -v grep|awk \'{print $1}\'',shell=True)
             r = str(q)
             r = r[2:-3]
             if r and int(r):
                      subprocess.call('kill -9 ' + r,shell=True)
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
button.place(x = 180, y = 20, height=35, width=59)

q.pack()
l2 = Label(width=3)
l2.place(x=270, y=65)

button2 = Button(root, text='Connect',command=var2)
button2.place(x = 180, y = 80, height=35, width=59)

buttonping2 = Button(root, text='ping', command=ping2)
buttonping2.place(x = 250, y = 85)
root.mainloop()
