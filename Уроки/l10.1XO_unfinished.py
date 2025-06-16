from tkinter import *

tk = Tk()

tk.title("Tkinter TEST") # Название программы вверху






buttons = StringVar()

button1 = Button(tk, text=' ', font='Times 26 bold', height=4, width=8)
button1.grid(row=0, column=0)
button1 = Button(tk, text=' ', font='Times 26 bold', height=4, width=8)
button1.grid(row=0, column=1)
button1 = Button(tk, text=' ', font='Times 26 bold', height=4, width=8)
button1.grid(row=0, column=2)
button1 = Button(tk, text=' ', font='Times 26 bold', height=4, width=8)
button1.grid(row=1, column=0)
button1 = Button(tk, text=' ', font='Times 26 bold', height=4, width=8)
button1.grid(row=1, column=1)
button1 = Button(tk, text=' ', font='Times 26 bold', height=4, width=8)
button1.grid(row=1, column=2)
button1 = Button(tk, text=' ', font='Times 26 bold', height=4, width=8)
button1.grid(row=2, column=0)
button1 = Button(tk, text=' ', font='Times 26 bold', height=4, width=8)
button1.grid(row=2, column=1)
button1 = Button(tk, text=' ', font='Times 26 bold', height=4, width=8)
button1.grid(row=2, column=2)




tk.mainloop()

"""
1. Ігрове поле
2. Самі фігури
3. Моєливість робити ходи
4. Перевірка виграшних комбінацій
5. Фінальний результат
6. Нічья
"""