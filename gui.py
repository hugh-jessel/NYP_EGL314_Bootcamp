import tkinter as tk
import osc_client

def function1():
    print("this is function 1")

def function2():
    print("this is function2")

def function3():
    print("this is function 3")   

def volume_change(x):
    global var
    if x == 1:
        if var == 50:
            var = var
            print("You cannot go any higher, Volume is already at " + str(var))
        else:
            var = var + 1
            print(var)
    
    else:
        if var == 0:
            var = var
            print("You cannot go any lower, Volume is already at " + str(var))
        else:
            var = var - 1
            print(var)

def call_osc():
    osc_client.quanfeng()

main = tk.Tk()
var = 0

title = tk.Label(main, text="NYP OSC DEMO CLASS", font="20")
title.grid(row=0,column=0, columnspan=3)

button1 = tk.Button(main, text="Function 1", font="12", command=function1)
button2 = tk.Button(main, text="Function 2", font="12", command=function2)
button3 = tk.Button(main, text="Function 3", font="12", command=function3)

VolumeUp = tk.Button(main, text="Volume +", font="12", command=lambda m=1:volume_change(m))
VolumeDown = tk.Button(main, text="Volume -", font="12", command=lambda m=0:volume_change(m))

osc = tk.Button(main, text="OSC", font="12", command=call_osc)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
VolumeUp.grid(row=2,column=0)
VolumeDown.grid(row=2, column=2)
osc.grid(row=3,column=1)

main.mainloop()