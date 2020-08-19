import tkinter as tk 
import tkinter.ttk as ttk 
#############################
def start():
    pass


root = tk.Tk()

note = ttk.Notebook(root)
note.grid(row=0, column=0)
##timer#######patient###########################
timer = tk.Frame()
patient = tk.Frame()
##########note#####################################
note.add(timer, text='Timer')
note.add(patient, text='patient')
############label###################################
B1 = tk.StringVar()
B1.set('patient1')
tk.Label(timer, textvariable=B1).grid(row=0, column=0)

B2 = tk.StringVar()
B2.set('patient2')
tk.Label(timer, textvariable=B2).grid(row=0, column=1)

B3 = tk.StringVar()
B3.set('patient3')
tk.Label(timer, textvariable=B3).grid(row=0, column=2)
####################################################
l1 = tk.StringVar()
l1.set('00:00')
tk.Label(timer, textvariable=l1).grid(row=1, column=0)
#####################################################
l2 = tk.StringVar()
l2.set('00:00')
tk.Label(timer, textvariable=l2).grid(row=1, column=1)
######################################################
l3 = tk.StringVar()
l3.set('00:00')
tk.Label(timer, textvariable=l3).grid(row=1, column=2)
#################button###############################
tk.Button(timer, text='start', command=start).grid(row=2, column=0)
################
tk.Button(timer, text='start', command=start).grid(row=2, column=1)
################
tk.Button(timer, text='start', command=start).grid(row=2, column=2)
##################timer last row cancel button############
tk.Button(timer, text='cancel', command=root.destroy).grid(row=3, column=0, columnspan=3 )
##########################################################
patient1 = tk.labelframe(patient, text='patient')
patient1.grid(row=-0, padx=10)





















root.mainloop()
