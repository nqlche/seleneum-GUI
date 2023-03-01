import tkinter as tk
from tkinter import messagebox
from tgstat_selenium import dowloand_data


def pars():
    try:
        url = entry1.get()
        file_name = entry2.get()
        dowloand_data(url=url, file_name=file_name)
        messagebox.showinfo('Готово', 'Файл создан в папке с парсером')
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
    except Exception:
        messagebox.showinfo('Ошибка', 'Проверьте корректность ссылки и названия файла')


win = tk.Tk()
win.geometry('445x500+400+200')
win.resizable(False, False)
win['bg'] = '#2C3339'
win.title('Парсер')

lable1 = tk.Label(win, text='Введите ссылку:', font=('Arial', 15), justify=tk.LEFT)
entry1 = tk.Entry(win, justify=tk.LEFT, font=('Arial', 15), width=40)
lable2 = tk.Label(win, text='Введите имя файла для сохранения:', font=('Arial', 15), justify=tk.LEFT)
entry2 = tk.Entry(win, justify=tk.LEFT, font=('Arial', 15), width=40)
btn = tk.Button(win, text='Запустить', font=('Arial', 15), command=pars)

lable1.grid(row=0, column=0, sticky='w', pady=5)
entry1.grid(row=1, column=0, pady=5)
lable2.grid(row=2, column=0, sticky='w', pady=5)
entry2.grid(row=3, column=0, pady=5)
btn.grid(row=4, column=0, pady=10)

win.mainloop()
