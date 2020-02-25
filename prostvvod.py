import tkinter as tk


def func():
        x = float(entry_1.get())
        y = float(entry_2.get())
        b=x+y 
        label.config(text="Сумма числе будет равна {}".format(b))



root = tk.Tk()
entry_1 = tk.Entry(root)
entry_2 = tk.Entry(root)
entry_1.grid(column=0, row=0)
entry_2.grid(column=1, row=0)

label = tk.Label(root, text="Сумма числе будет равна")
label.grid(column=2, row=2)
label2 = tk.Label(root, text="масса")
label2.grid(column=1, row=1)

label3 = tk.Label(root, text="скорость")
label3.grid(column=0, row=1)

button = tk.Button(root, text='сложить числа', command=func)
button.grid(column=2, row=3)
root.mainloop()