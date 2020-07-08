import tkinter as tk

def turn():
    print(1)


root = tk.Tk()

lk = tk.Label(root,text='')
lk.pack()


ln = tk.Button(root,text='Get turn!',command=turn)
ln.pack()

root.mainloop()