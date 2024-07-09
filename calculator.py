from tkinter import *

expr = ""

def btnclk(n):
    global expr
    expr += str(n)
    v.set(expr)

def calculate():
    global expr
    try:
        result = eval(expr)
        v.set(result)
        expr = str(result)
    except:
        v.set("Error")
        expr = ""

def clear():
    global expr
    expr = ""
    v.set(expr)

w = Tk()
w.configure(bg='aqua')
w.title("Calculator")

v = StringVar()

E = Entry(w, font=("arial", 20, "bold"), bg="#dcedc8", relief="solid", border=3, textvariable=v, justify='right')


button_params = {
    'font': ("arial", 15, "bold"),
    'relief': 'raised',
    'bd': 3,
    'width': 4,
    'height': 2
}


func_button_params = button_params.copy()
func_button_params.update({'bg': '#ff8a80', 'fg': 'white'})

num_button_params = button_params.copy()
num_button_params.update({'bg': '#424242', 'fg': 'white'})

equal_button_params = button_params.copy()
equal_button_params.update({'bg': '#ffab40', 'fg': 'white'})
clear_button_params = button_params.copy()
clear_button_params.update({'bg': '#ff5252', 'fg': 'white'})

B1 = Button(w, text="1", command=lambda: btnclk(1), **num_button_params)
B2 = Button(w, text="2", command=lambda: btnclk(2), **num_button_params)
B3 = Button(w, text="3", command=lambda: btnclk(3), **num_button_params)
B4 = Button(w, text="4", command=lambda: btnclk(4), **num_button_params)
B5 = Button(w, text="5", command=lambda: btnclk(5), **num_button_params)
B6 = Button(w, text="6", command=lambda: btnclk(6), **num_button_params)
B7 = Button(w, text="7", command=lambda: btnclk(7), **num_button_params)
B8 = Button(w, text="8", command=lambda: btnclk(8), **num_button_params)
B9 = Button(w, text="9", command=lambda: btnclk(9), **num_button_params)
B0 = Button(w, text="0", command=lambda: btnclk(0), **num_button_params)
Bdot = Button(w, text=".", command=lambda: btnclk('.'), **num_button_params)

Bequals = Button(w, text="=", command=calculate, **equal_button_params)
Bclear = Button(w, text="C", command=clear, **clear_button_params)
Bplus = Button(w, text="+", command=lambda: btnclk('+'), **func_button_params)
Bmin = Button(w, text="-", command=lambda: btnclk('-'), **func_button_params)
Bmul = Button(w, text="*", command=lambda: btnclk('*'), **func_button_params)
Bdiv = Button(w, text="/", command=lambda: btnclk('/'), **func_button_params)


E.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


Button(w, text="mrc", **func_button_params).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
Button(w, text="m-", **func_button_params).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
Button(w, text="m+", **func_button_params).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
Bdiv.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")


buttons = [
    (B7, 2, 0), (B8, 2, 1), (B9, 2, 2), (Bmul, 2, 3),
    (B4, 3, 0), (B5, 3, 1), (B6, 3, 2), (Bmin, 3, 3),
    (B1, 4, 0), (B2, 4, 1), (B3, 4, 2), (Bplus, 4, 3),
    (B0, 5, 0), (Bdot, 5, 1), (Bclear, 5, 2), (Bequals, 5, 3),
]

for (btn, row, col) in buttons:
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


for i in range(4):
    w.columnconfigure(i, weight=1)
for i in range(6):
    w.rowconfigure(i, weight=1)

w.mainloop()
