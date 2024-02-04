import tkinter as tk
from math import floor
# Значение x должно быть в пределах от 54.6 до 100
def validate_x(x):
    try:
        x = float(x)
        if 54.6 <= x <= 100:
            return True
        else:
            return False
    except ValueError:
        return False

# Значение k должно быть в пределах от 1 до 9
def validate_k(k):
    try:
        k = float(k)
        if 1 <= k <= 9:
            return True
        else:
            return False
    except ValueError:
        return False

def calculate_y():
    x = entry_x.get()
    k = entry_k.get()

    if validate_x(x) and validate_k(k):
        x = float(x)
        k = float(k)
        y = floor((x - 54.6) * 66 * k / 2) * 2
        result_label.config(text=f"Необходимо внести воды: {y}")
    else:
        result_label.config(text="Некорректные значения ,исправьте")
        

# Создание окна приложения
window = tk.Tk()

# Название программы
title_label = tk.Label(window, text="Кола Добрый SMR 1.01", font=("Arial", 16))
title_label.pack()

# Создание элементов интерфейса
label_x = tk.Label(window, text="Введите Брикс сиропа:",font=("Arial",10))
entry_x = tk.Entry(window)

label_k = tk.Label(window, text="Введите кол-во единиц колы:",font=("Arial",10))
entry_k = tk.Entry(window)

button = tk.Button(window, text="Вычислить", command=calculate_y)

result_label = tk.Label(window, text="")

# Размещение элементов по середине
title_label.pack(side="top", pady=100)
label_x.pack()
entry_x.pack()
label_k.pack()
entry_k.pack()
button.pack()
result_label.pack()



# Запуск главного цикла приложения
window.mainloop()
