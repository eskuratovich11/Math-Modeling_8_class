import tkinter as tk
from PIL import Image, ImageTk 
 
window = tk.Tk()
window.title("Кто лишний?")  
window.geometry('400x250')  
 
mainmenu = tk.Menu(window) 
window.config(menu=mainmenu) 

lbl1 = tk.Label(window) 
lbl1.grid(column=0, row=1)  
lbl2 = tk.Label(window) 
lbl2.grid(column=0, row=1)   
image = Image.open("nuton2.jpg")
photo = ImageTk.PhotoImage(image)

def clicked():  
    label = tk.Label(image=photo)
    label.image = photo 
    label.grid(column=0, row=1)
def clicked2():  
    lbl1.configure(text='Планеты и Солнце')    
def clicked3():  
    lbl2.configure(text='Солнечная система')     
    
    
def clicked4():  
    root = tk.Tk()
    entry_1 = tk.Entry(root)
    entry_2 = tk.Entry(root)
    entry_3 = tk.Entry(root)
    entry_1.grid(column=1, row=0)
    entry_2.grid(column=1, row=1)
    entry_3.grid(column=1, row=2)
    
    label1 = tk.Label(root, text="масса")
    label1.grid(column=0, row=0)

    label2 = tk.Label(root, text="скорость")
    label2.grid(column=0, row=1)

    label3 = tk.Label(root, text="расстояние до Солнца")
    label3.grid(column=0, row=2)
    
def clicked5():  
    root = tk.Tk()
    entry_1 = tk.Entry(root)
    entry_2 = tk.Entry(root)
    entry_3 = tk.Entry(root)
    entry_1.grid(column=1, row=0)
    entry_2.grid(column=1, row=1)
    entry_3.grid(column=1, row=2)
    
    label1 = tk.Label(root, text="масса")
    label1.grid(column=0, row=0)

    label2 = tk.Label(root, text="скорость")
    label2.grid(column=0, row=1)

    label3 = tk.Label(root, text="расстояние до Солнца")
    label3.grid(column=0, row=2)
    
def clicked6():  
    root = tk.Tk()
    entry_1 = tk.Entry(root)
    entry_2 = tk.Entry(root)
    entry_3 = tk.Entry(root)
    entry_1.grid(column=1, row=0)
    entry_2.grid(column=1, row=1)
    entry_3.grid(column=1, row=2)
    
    label1 = tk.Label(root, text="масса")
    label1.grid(column=0, row=0)

    label2 = tk.Label(root, text="скорость")
    label2.grid(column=0, row=1)

    label3 = tk.Label(root, text="расстояние до Солнца")
    label3.grid(column=0, row=2)
    
    
    
    
infmenu = tk.Menu(mainmenu, tearoff=0)
infmenu.add_command(label="Сила всемирного тяготения", command=clicked)
infmenu.add_command(label="Что есть в Солнечной системе?", command=clicked2)
infmenu.add_command(label="Солнечная система", command=clicked3)

animmenu = tk.Menu(mainmenu, tearoff=0)
animmenu.add_command(label="Добавим планету", command=clicked4)
animmenu.add_command(label="Новая звезда", command=clicked5)
animmenu.add_command(label="Второе Солнце", command=clicked6)


mainmenu.add_cascade(label="Информация", menu=infmenu)
mainmenu.add_cascade(label="Эксперименты", menu=animmenu)

 
window.mainloop() 