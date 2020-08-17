import tkinter as tk 
import tkinter.ttk as ttk 
#############################
root = tk.Tk()

note = ttk.Notebook(root)
note.grid(row=0, column=0)
##timer#######patient########
timer = tk.Frame()
patient = tk.Frame()
##########note###############
note.add(timer, text='Timer')
note.add(patient, text='patient')
############label##################
B1 = tk.StringVar()
B1.set('patient1')
tk.Label(timer, textvariable=B1).grid(row=0, column=0)

B2 = tk.StringVar()
B2.set('patient2')
tk.Label(timer, textvariable=B2).grid(row=0, column=1)

B3 = tk.StringVar()
B3.set('patient3')
tk.Label(timer, textvariable=B3).grid(row=0, column=2)

root.mainloop()
