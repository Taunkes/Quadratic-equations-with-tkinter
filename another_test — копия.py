from math import sqrt
import tkinter
from tkinter import messagebox


def solve():
    try:
        a, b, c = float(u.get()), float(l.get()), float(t.get())
    except ValueError:
        messagebox.showerror('Ошибка',
'''⠄⣾⣿⡇⢸⣿⣿⣿⠄⠈⣿⣿⣿⣿⠈⣿⡇⢹⣿⣿⣿⡇⡇⢸⣿⣿⡇⣿⣿⣿
⢠⣿⣿⡇⢸⣿⣿⣿⡇⠄⢹⣿⣿⣿⡀⣿⣧⢸⣿⣿⣿⠁⡇⢸⣿⣿⠁⣿⣿⣿
⢸⣿⣿⡇⠸⣿⣿⣿⣿⡄⠈⢿⣿⣿⡇⢸⣿⡀⣿⣿⡿⠸⡇⣸⣿⣿⠄⣿⣿⣿
⢸⣿⡿⠷⠄⠿⠿⠿⠟⠓⠰⠘⠿⣿⣿⡈⣿⡇⢹⡟⠰⠦⠁⠈⠉⠋⠄⠻⢿⣿
⢨⡑⠶⡏⠛⠐⠋⠓⠲⠶⣭⣤⣴⣦⣭⣥⣮⣾⣬⣴⡮⠝⠒⠂⠂⠘⠉⠿⠖⣬
⠈⠉⠄⡀⠄⣀⣀⣀⣀⠈⢛⣿⣿⣿⣿⣿⣿⣿⣿⣟⠁⣀⣤⣤⣠⡀⠄⡀⠈⠁
⠄⠠⣾⡀⣾⣿⣧⣼⣿⡿⢠⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣧⣼⣿⣿⢀⣿⡇⠄
⡀⠄⠻⣷⡘⢿⣿⣿⡿⢣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⢿⣿⣿⡿⢃⣾⠟⢁⠈
⢃⢻⣶⣬⣿⣶⣬⣥⣶⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣷⣾⣾⢣
⡄⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠘
⣿⡐⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢠⢃
⣿⣷⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⠆⣼
⣿⣿⣷⡀⠄⠈⠛⢿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⠿⠋⠠⠂⢀⣾⣿
⣿⣿⣿⣧⠄⠄⢵⢠⣈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⡁⢰⠏⠄⠄⣼⣿⣿
⢻⣿⣿⣿⡄⢢⠨⠄⣯⠄⠄⣌⣉⠛⠻⠟⠛⢋⣉⣤⠄⢸⡇⣨⣤⠄⢸⣿⣿⣿
⡏⠉⠉⠉⠉⠉⠉⠋⠉⠉⠉⠉⠉⠉⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠉⠉⠉⠹
⡇⢸⣿⡟⠛⢿⣷⠀⢸⣿⡟⠛⢿⣷⡄⢸⣿⡇⠀⢸⣿⡇⢸⣿⡇⠀⢸⣿⡇⠀
⡇⢸⣿⣧⣤⣾⠿⠀⢸⣿⣇⣀⣸⡿⠃⢸⣿⡇⠀⢸⣿⡇⢸⣿⣇⣀⣸⣿⡇⠀
⡇⢸⣿⡏⠉⢹⣿⡆⢸⣿⡟⠛⢻⣷⡄⢸⣿⡇⠀⢸⣿⡇⢸⣿⡏⠉⢹⣿⡇⠀
⡇⢸⣿⣧⣤⣼⡿⠃⢸⣿⡇⠀⢸⣿⡇⠸⣿⣧⣤⣼⡿⠁⢸⣿⡇⠀⢸⣿⡇⠀
⣇⣀⣀⣀⣀⣀⣀⣄⣀⣀⣀⣀⣀⣀⣀⣠⣀⡈⠉⣁⣀⣄⣀⣀⣀⣠⣀⣀⣀⣰''')
        return

    d = b ** 2 - 4 * a * c

    if d > 0:
        try:
            label["text"] = f"x1 = {(-b + sqrt(d)) / (2 * a)} and x2 = {-b - sqrt(d)}"
        except ZeroDivisionError:
            label["text"] = f"x1 = {(-b + sqrt(d)) / (2 * 1)} and x2 = {-b - sqrt(d)}"
    elif d == 0:
        label["text"] = f"x = {-b / (2 * a)}"

    else:
        label["text"] = "Waaa Корней нет"


window = tkinter.Tk()
window.geometry('950x650')
window.title('Квадратные уравнения')
window.resizable(False, False)

label = tkinter.Label(width=60, font=10)
label.pack()
label2 = tkinter.Label(text="""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠛⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⢀⠀⠀⠀⢠⠀⠀⠀⠀⠉⠙⠿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠰⡄⠀⣃⣠⣤⣬⣆⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⣠⣀⠀⠀⠈⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠀⡴⢄⠀⠀⢠⣾⣿⣿⠿⠿⠿⣿⣿⣦⣽⣼⣀⣜⣠⣿⣿⣴⡄⠀⣽⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠠⢰⠆⢢⣤⣼⣿⣿⣧⣶⣶⡖⠀⠀⠀⢈⣿⣿⣯⣭⣭⠉⠉⠁⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠠⡀⢺⠸⢿⣿⣿⣿⣿⣿⣿⣥⣤⣤⣴⣿⣿⣿⣿⣿⣛⣀⣀⡀⣰⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⠣⠴⡾⢻⣿⣿⣿⣿⣿⣿⣟⠻⠿⠿⠛⠿⠿⢛⣿⣿⣿⠇⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⣿⣮⣛⣫⣵⣾⣿⣿⠿⠋⢠⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⡀⢰⣶⣿⣿⣟⠛⠛⠛⠛⠛⠋⠉⠀⠀⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢀⢸⣿⣦⣝⠻⡿⣡⣄⠀⠀⠀⠀⠀⠀⢐⠀⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⢀⣤⣴⣶⣿⡹⣿⣿⣿⡟⣵⢰⡟⣴⡆⠀⠀⠀⠀⠀⣸⠀⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⢀⣯⡻⣿⣿⣿⣿⣮⣝⣩⣾⣿⢎⣤⣙⣴⣿⣷⡄⠀⠀⣿⡆⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⡇⠀⠀⣿⣷⣌⡿⠿⣛⠻⢿⣿⣿⣿⢸⣿⣿⣿⡿⣡⡇⠐⠀⣿⣿⠀⣼⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⢀⢻⣿⢏⡶⣿⣿⣿⣷⡍⢿⡷⢟⣫⣭⡛⣰⣿⠣⠁⣸⣿⣿⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⢠⠀⡾⣸⣿⣎⢡⣿⢿⣿⡿⢛⣠⣾⣿⣿⣿⡇⣋⣭⣧⢺⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣸⢀⣇⢿⢸⣿⡘⠏⢼⡟⣰⣿⣿⣿⣿⣿⠟⣐⣻⣿⠋⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡁⣿⣿⣦⡘⣿⢸⣿⠌⣸⣿⣿⣿⡿⢋⣴⣿⣝⢿⣿⡔⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⣬⣛⠿⣷⡍⣾⣿⠀⣿⣿⠿⣫⣔⢿⣿⣿⣿⢘⣿⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⢡⣬⣉⣛⠲⠶⠜⣛⣒⣤⣤⣛⣛⣿⣆⣉⡛⠉⣈⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⢿⣿⣿⣿⢻⣷⣶⠆⣤⣤⣤⡄⢠⣤⣤⣤⣄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡏⠄⣿⣿⣿⡏⢸⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⢠⢠⣿⣿⣿⠃⣺⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠄⢸⣿⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⣧⢸⣿⣿⣿⣿⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣦⡀⣭⣭⣭⣭⣤⣭⡍⠉⠀⠛⠛⠻⠿⠈⣥⣤⣤⠀⠀⠼⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⣿⣿⣿⣿⣿⣤⣤⣝⠻⣿⣿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⠛⠿⠸⢿⣿⣿⣿⣿⣿⣿⣿⠿⢟⣸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣮⣍⣛⣛⠛⠿⠿⢛⣋⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣬⣿⣿⣿⣿⣿⣿⣿""")
label3 = tkinter.Label(text=
                       """⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣥⣷⣶⣾⣿⣿⣶⣾⣬⣙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⣻⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡌⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⢥⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠇⣾⣏⣀⠄⠄⠄⢀⣿⣿⣿⡁⠄⠄⠄⠄⣉⣹⣿⠄⢡⣙⢿⣿⣿⣿
⣿⣿⣿⡿⢸⣿⢋⠄⠄⠄⠄⢀⣿⣿⣿⡀⠄⠄⠄⠄⢈⠙⣿⠄⢸⣿⣧⠽⣿⣿
⣿⣿⣿⡷⣿⣿⣿⣿⣯⣴⣾⣿⣿⣿⣿⣿⣶⣶⣤⣶⣿⣿⣿⠄⠈⣿⣿⣧⣻⣿
⣿⣿⣿⡧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⠄⢸⣿⣿⣿⠼⣿
⣿⣿⣿⡟⣿⣿⡿⠋⢼⣿⣿⠾⠛⠛⠁⠈⠁⡓⠛⢿⣿⣿⡟⠄⣼⣿⣿⣿⣇⢿
⣿⣿⣿⠧⣿⣿⣇⠄⢛⣻⣿⣿⠶⠒⠓⠒⢒⠓⠄⠸⣿⣿⡇⢰⣿⣿⣿⣿⣿⢹
⣿⣿⣿⠄⣿⣿⣿⣷⣿⣿⣿⣿⠿⠛⢛⣿⣿⣷⣦⣿⡿⣿⡇⠘⠛⠛⢿⣿⢿⣸
⣿⣿⣿⡄⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⡾⠿⠿⠿⠟⠁⠄⠄⠄⢠⣬⣭⣤⣼⣾⣿
⣿⣿⣿⡇⣿⣿⠟⠟⠿⠏⠉⠉⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠃⢸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡯⠘⡍⠁⠄⠄⠄⠄⢀⣀⣀⣀⣀⠄⠄⠄⠄⠄⠄⠄⣸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡀⠁⠄⠄⠄⠄⣠⣿⣿⣿⣿⣿⣄⠄⠄⠄⠄⠄⣨⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⣄⣀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿""")

u, l, t = tkinter.Entry(width=40), tkinter.Entry(width=40), tkinter.Entry(width=40)
u.pack()
l.pack()
t.pack()

button = tkinter.Button(text='Посчитать', command=solve, width=15)
button.pack()
label2.place(relx=0.35, rely=0.5, anchor='center')
label3.place(relx=0.65, rely=0.68, anchor='center')
window.mainloop()
