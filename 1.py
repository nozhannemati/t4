import tkinter as tk
from datetime import datetime


def turn():
    global n
    n +=1
    numbers.append(n + 1)
    print(numbers)
    d = datetime.now()

    l1.config(text=d.strftime("%B/%d/%Y"))

    a1.config(text=d.strftime("%-H:%-M:%-S"))

    c1.config(text=d.strftime("%A"))

    e1.config(text='Your Turn:' + str(numbers[-1]))

    e2.config(text='left:' + str(len(numbers)-1))

    line = '{},{},{}\n'.format(numbers[-1],
                              d.strftime("%-H:%-M:%-S"),
                              d.strftime('%-m:%-M:%-S'))


    with open ('turns.csv','a') as file:
        file.write(line)


def append_csv(numbers, operators):
    d = datetime.now()
    line = '{},{},{},numbers{}\n'.format(numbers[-1],
                               d.strftime("%-H:%-M:%-S"),
                               d.strftime('%-m:%-M:%-S'),
                               operator)







def op1():
    if numbers:
      number = numbers.pop(0)
      Lo1.config(text=number)
      append_csv(numbers, 1)


def op2():
   if numbers:
     number = numbers(0)
     Lo2.config(text=number)
     append_csv(numbers, 2)

def op3():

    if numbers:
      number = numbers.pop(0)
      Lo3.config(text=number)
      append_csv(numbers, 3)

root = tk.Tk()
n = -1
numbers = []

l1 = tk.Label(root, text='')
l1.grid(row=0, column=0)

a1 = tk.Label(root, text='')
a1.grid(row=1, column=0)

c1 = tk.Label(root, text='')
c1.grid(row=2, column=0)

e1 = tk.Label(root, text='')
e1.grid(row=3, column=0)

e2 = tk.Label(root, text='')
e2.grid(row=4, column=0)

b1 = tk.Button(root, text='Get Turn!', command=turn)
b1.grid(row=5, column=0)

tp = tk.Toplevel(root)

o1 = tk.Button(tp, text='operator1', command=op1)
o1.grid(row=0, column=0)

o2 = tk.Button(tp, text='operator2', command=op2)
o2.grid(row=0, column=1)

o3 = tk.Button(tp, text='operator3', command=op3)
o3.grid(row=0, column=2)

Lo1 = tk.Label(tp, text='--')
Lo1.grid(row=1, column=0)
Lo2 = tk.Label(tp, text='--')
Lo2.grid(row=1, column=1)
Lo3 = tk.Label(tp, text='--')
Lo3.grid(row=1, column=2)


root.mainloop()
