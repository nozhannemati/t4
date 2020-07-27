import tkinter as tk
root = tk.Tk()

def stop():
    pass



tk.Label(root,
         text='left player').grid(row=0, column=0)

tk.Label(root,
         text='right player').grid(row=0, column=1)

L.timer = tk.StringVar()
L.timer.set('20:00')
tk.Label(root,
         textvarible='l_timer').grid(row=0, column=0)
R.timer = tk.StringVar()
R.timer.set('20:00')
tk.Label(root,
         textvarible='r_timer').grid(row=1, column=1)

tk.Button(root, text='start').grid(row=1, clumn=2)

tk.Button(root, text='cancel').grid(row=4, culomn=0)

tk.Button(root,
          text='stop',
          commmand=stop).grid(row=2, column=0)

tk.Button(root,
          text='stop',
          commmand=stop).grid(row=2, column=2)


root.mainloop()