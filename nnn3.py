import tkinter as tk
from threading import Thread
from time import sleep


def stop(side):
    global flag
    if side == 'left':
        flag = True
    else:
        flag = False






def start(t):
    while True:
        sleep(1)
        if flag:
            timer['right']  -=1
            m, s = divmod(timer['right'], 60)

            R_timer.set('%02d:%02d' %(m, s))
        else:
            timer['left'] -=1
            m, s = divmod(timer['left'], 60)

            L_timer.set('%02d:%02d' % (m, s))




root = tk.Tk()




timer = {'left':1200,
         'right':1200}


flag = False


tk.Label(root,
         text='left player').grid(row=0, column=0)



tk.Label(root,
         text='right player').grid(row=0, column=1)


L_timer = tk.StringVar()
L_timer.set('20:00')


tk.Label(root,
         textvariable=L_timer).grid(row=1, column=0)


R_timer = tk.StringVar()
R_timer.set('20:00')



tk.Label(root,
         textvariable=R_timer).grid(row=1,column=1)


tk.Button(root, text='cancel',command= root.destroy).\
    grid(row=4, column=0,columnspan=2)



tk.Button(root,
          text='stop',
          command=lambda:stop('left')).grid(row=2, column=0)


tk.Button(root,
          text='stop',
          command=lambda:stop('right')).grid(row=2, column=1)





thread1 = Thread(target=start, args=(0, ))
thread1.start()
root.mainloop()