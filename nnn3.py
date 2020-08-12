import tkinter as tk
from threading import Thread
from time import sleep


########################################################################################################################
def stop(side):
    global flag
    if side == 'left':
        flag = True
    else:
        flag = False
    ####################################################################################################################


def start(val):
    timer['left'] = timer['right'] = val
    while True:
        if timer['left'] == 0 or timer['right'] == 0:
            break

        sleep(1)
        if flag:
            timer['right'] -= 1
            m, s = divmod(timer['right'], 60)

            r_timer.set('%02d:%02d' % (m, s))
        else:
            timer['left'] -= 1
            m, s = divmod(timer['left'], 60)  #
            l_timer.set('%02d:%02d' % (m, s))


#########################################################
def begin():
    value = time_value.get()
    thread1 = Thread(target=start, args=(value,))
    thread1.start()

    m, s = divmod(Value, 60)

    l_timer.set('%02d:%02d' % (m, s))
    r_timer.set('%02d:%02d' % (m, s))

root = tk.Tk()
##########################################################
timer = {'left':
             'right'}
flag = False

#########T################################################
l_timer = tk.StringVar()
l_timer.set("00:00")
r_timer = tk.StringVar()
r_timer.set("00:00")

#######label##############################################
tk.Label(root, text="Left player", font=("times", 15,)).grid(row=0, column=0)
tk.Label(root, text="Right player", font=("times", 15,)).grid(row=0, column=2, sticky=tk.N + tk.E)

#####label################################################
tk.Label(root, textvariable=l_timer).grid(row=1, column=0)
tk.Label(root, textvariable=r_timer).grid(row=1, column=2)

time_value = tk.IntVar()
tk.Entry(root,
         textvariable=time_value,
         font=('times', 20)).grid(row=3, column=0, columnspan=2)
######button##############################################
tk.Button(root, text="stop", bg="red", command=lambda: stop('left'), font=("times", 15,)).grid(row=2, column=0)
tk.Button(root, text="stop", bg="red", command=lambda: stop('right'), font=("times", 15,)).grid(row=2, column=2)
tk.Button(root, text="start", bg="yellow", command=begin, font=("times", 15,)).grid(row=4, column=1)
tk.Button(root, text="cancel", bg="yellow", command=root.destroy, font=("times", 15,)).grid,

########################################################################################################################
root.mainloop()
