import tkinter as tk               
import tkinter.ttk as ttk          



bgak ={"bg" :"#91ff35"}    
bgak1 = {'bg' : "#f50057", 'font':'helvetica'}
                                   
                                   
                                
root = tk.Tk()                     



note = ttk.Notebook()               
note.grid(row=0, column=0)        



food = tk.Frame()                 
f1 = tk.Frame(food, cnf=bgak)
f1.grid(row =0, column=0)

reciept= tk.Frame()               


drink = tk.Frame()                 



note.add(drink, text='drink')     
note.add(food, text='food')        
note.add(reciept, text='reciept') 



tk.Label(f1, text='ghorme sabzi',cnf=bgak).grid(row=0,column=0)
tk.Label(f1, text='⭐⭐⭐⭐⭐(45)',cnf=bgak).grid(row=1, column=0)
tk.Label(f1, text='1.2 $', cnf=bgak).grid(row=2, column=0)



root.mainloop()          