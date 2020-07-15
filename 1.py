import tkinter as tk
from datetime import datetime


def turn():
    numbers.append(len(numbers)+1)
    print(numbers)
    d = datetime.now()

    l1.config(text=d.strftime("%B/%d/%Y"))

    a1.config(text=d.strftime("%-H:%-M:%-S"))

    c1.config(text=d.strftime("%A"))

    e1.config(text='Your Turn:'+str(numbers[-1]))


root = tk.Tk()
numbers=[]

l1 = tk.Label(root, text='')
l1.grid(row=0, column=0)

a1 = tk.Label(root, text='')
a1.grid(row=, column=0)

c1= tk.Label(root, text = '')
c1.pack()

e1= tk.Label(root, text='')
e1.pack()

b1 = tk.Button(root, text='Get Turn!', command=turn)
b1.pack()



root.mainloop()
