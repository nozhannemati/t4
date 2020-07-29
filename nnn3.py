import tkinter as tk

def stop():
    pass

root = tk.Tk()

timer = {'left':1200,
         'right':1200}




tk.Label(root,
         text='left player').grid(row=0, column=0)

tk.Label(root,
         text='right player').grid(row=0, column=1)

L_timer = tk.StringVar()
L_timer.set('20:00')
tk.Label(root,
         textvariable='L_timer').grid(row=1, column=0)
R_timer = tk.StringVar()
R_timer.set('20:00')
tk.Label(root,
         textvariable='r_timer').grid(row=1,column=1)

tk.Button(root, text='start').grid(row=3,column=0,columnspan=2)

tk.Button(root, text='cancel',command= root.destroy).grid(row=4, column=0,columnspan=2)

tk.Button(root,
          text='stop',
          command=stop).grid(row=2, column=1)

tk.Button(root,
          text='stop',
          command=stop).grid(row=2, column=2)


root.mainloop()