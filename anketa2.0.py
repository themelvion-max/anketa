import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def submit_form():
    """Функция сбора данных из формы с сохранением текстового файла."""
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    job = combo_job.get()
    is_subscribed = "Да" if subscribe_var.get() else "Нет"

    if name and age:
        #формируем строку для записей
        data_str = (f"ФИО: {name}\n"
                    f"Возраст: {age}\n"
                    f"Пол: {gender}\n"
                    f"Профессия: {job}\n"
                    f"Подписка на новости: {is_subscribed}\n"
                    f"{'-'*20}\n") #азделитель между анкетами

        try:
            with open("Анкеты_пользователей.txt", "a", encoding="utf-8") as file:
                file.write(data_str)
                    
            messagebox.showinfo("Успех", "Данные успешно сохраненны в файле Анкеты_пользователей.txt ")

#Очищаем поля после сохранения
            entry_name.delete(0, tk.END)
            entry_age.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Ошибка файла", f"Не удалось сохранить: {e}")
    else:
        messagebox.showwarming("Внимание", "Заполните обязательные поля!")

# создаём окно с нуля
root=tk.Tk()
root.title("Анкета пользователя")
root.geometry("400x450")
import os
import sys

# Определяем путь к папке, где лежит сам скрипт
base_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_path, "favicon.ico")

# Проверяем, существует ли файл, прежде чем устанавливать иконку
if os.path.exists(icon_path):
    root.wm_iconbitmap(icon_path)
else:
    print(f"Предупреждение: Файл иконки не найден по пути: {icon_path}")

# общий контейнер с отступами
main_frame=tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill="both")

# Личные данные
personal_info=tk.LabelFrame(main_frame, text="Личная информация", padx=10, pady=10)
personal_info.pack(fill="x", pady=10)

tk.Label(personal_info, text="ФИО:").grid(row=0, column=0, sticky="w")
entry_name=tk.Entry(personal_info)
entry_name.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

tk.Label(personal_info, text="Возраст:").grid(row=1, column=0, sticky="w")
entry_age=tk.Entry(personal_info, width=5)
entry_age.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# выбор (radiobutton)
gender_frame=tk.LabelFrame(main_frame, text="Пол", padx=10, pady=10)
gender_frame.pack(fill="x", pady=10)

gender_var=tk.StringVar(value="Мужской")
tk.Radiobutton(gender_frame, text="Мужской", variable=gender_var, value="Мужской").pack(side="left")
tk.Radiobutton(gender_frame, text="Женский", variable=gender_var, value="Женский").pack(side="left")

# дополнительно
extra_frame=tk.Frame(main_frame)
extra_frame.pack(fill="x", pady=10)

tk.Label(extra_frame, text="Профессия:").pack(side="left")
combo_job=ttk.Combobox(extra_frame, values=["Программист", "Дизайнер", "Менеджер", "Школьник"])
combo_job.pack(side="left", padx=10)
combo_job.current(0)

# Чекбокс
subscribe_var=tk.BooleanVar()
check_sub=tk.Checkbutton(main_frame, text="Подписаться на рассылку", variable=subscribe_var)
check_sub.pack(pady=10)

# кнопка отправки
btn_submit=tk.Button(main_frame, text="Отправить анкету", bg="#4CAF50", fg="white",
                     font=("Arial", 12, "bold"), command=submit_form)
btn_submit.pack(fill="x", pady=20)




root.mainloop()

