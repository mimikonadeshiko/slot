import tkinter
import random
import time
import logging
from threading import Thread
from functools import partial
#2022.1.10.12:00
#V0.1

tki = tkinter.Tk()
tki.geometry('300x200')
tki.title('slot')

push1 = 0
push2 = 0
push3 = 0


i = 0
def start():
    print("START")
    global stop1
    thread = Thread(target=darararara, args=(logger,), name="SubThread", daemon=True)
    thread.start()
logger = logging.getLogger(__file__)
   
def darararara(logger, count=0, interval=0.7):
    txt.delete(0,tkinter.END)
    #"歯が抜けた"
    #print ("darararara")
    global push1
    countnow1 = 0
    countanswer1 = 0
    countnow2 = 0
    countanswer2 = 0
    countnow3 = 0
    countanswer3 = 0

    while 1:
        txt1.delete(0,tkinter.END)
        count += 1
        logger.info("Count: {:2}".format(count))
        
        #print("dararararaなう")
        #print(countnow1)
        if push1 == 1:
            countanswer1 = countnow1
        #    print (countanswer1)
            txt1.insert(tkinter.END,countanswer1)
        elif push1 == 0:
            countnow1 = random.randint(1,9)
            txt1.insert(tkinter.END,countnow1)

        txt2.delete(0,tkinter.END)
        if push2 == 1:
            countanswer2 = countnow2
        #    print (countanswer2)
            txt2.insert(tkinter.END,countanswer2)
        elif push2 == 0:
            countnow2 = random.randint(1,9)
            txt2.insert(tkinter.END,countnow2)

        txt3.delete(0,tkinter.END)
        if push3 == 1:
            countanswer3 = countnow3
        #    print (countanswer3)
            txt3.insert(tkinter.END,countanswer3)
        elif push3 == 0:
            countnow3 = random.randint(1,9)
            txt3.insert(tkinter.END,countnow3)

        if push1 == 1 and push2 == 1 and push3 == 1:
            print("全部押されたよ!")
        #    print(countanswer1)
        #    print(countanswer2)
        #    print(countanswer3)
            if countanswer1 == countanswer2 and countanswer2 == countanswer3 and countanswer3 == countanswer1:
                txt.insert(tkinter.END,"おっめでとう!!")
            else:
                txt.insert(tkinter.END,"ざんねん...")
            break
            
        time.sleep(interval)

        
def stop1():
#    print("stop1")
    global push1
    push1 = 1
def stop2():
#    print("stop2")
    global push2
    push2 = 1
def stop3():
#    print("stop3")
    global push3
    push3 = 1


btn = tkinter.Button(tki, text='START', command=start)
btn.place(x=160, y=0)
btn.pack(fill = 'x', padx=20, side = 'top')
btn = tkinter.Button(tki, text='STOP', width=6, command=stop1)
btn.pack(fill = 'x', padx=20, side = 'left')
btn = tkinter.Button(tki, text='STOP', width=6, command=stop2)
btn.pack(fill = 'x', padx=20, side = 'left')
btn = tkinter.Button(tki, text='STOP', width=6, command=stop3)
btn.pack(fill = 'x', padx=20, side = 'left')
txt1 = tkinter.Entry(width=2)
txt1.place(x=35, y=50)
txt2 = tkinter.Entry(width=2)
txt2.place(x=130, y=50)
txt3 = tkinter.Entry(width=2)
txt3.place(x=230, y=50)
txt = tkinter.Entry(width=20)
txt.place(x=50, y=24)
tki.mainloop()
