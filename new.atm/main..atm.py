import tkinter as tk
import tkinter.ttk  as ttk

root = tk.Tk()
root.title("bank")


# top = tk.Toplevel()
# top.title("form")

Frame_top= tk.frame()
Frame_top=ttk.Notebook()

note = ttk.Notebook()


register_form = tk.Frame()
login_form = tk.Frame()


note.add(register_form, text="register")
note.add(login_form, text="log in ")
note.grid(row=0, column=0)
########...............########
tk.Label(register_form, text="username:").grid(row=0, column=0)
tk.Label(register_form, text='password:').grid(row=1, column=0)
form_user = tk.StringVar()
form_pass = tk.StringVar()
tk.Entry(register_form, textvariable=form_user).grid(row=0, column=0)
tk.Entry(register_form, textvariable=form_user).grid(row=1, column=1)
tk.Button(register_form, text="register").grid(row=1, column=0, columnspan=2, sticky=tk.w+tk.E)


root.mainloop 



