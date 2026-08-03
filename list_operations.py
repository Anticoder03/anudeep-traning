# l = [1,2,3,4,5,6,7,8,9]

# print(type(l))

# l.append(10)
# print(l)

# l.insert(0, 0)
# print(l)

# l.remove(5)
# print(l)

# l2 = ["A", "B", "C"]
# print(l2)

# l.extend(l2)
# print(l)

# l1 = [12,43,65,73,67,23]
# l1.sort()
# print(l1)

# l1.sort(reverse=True)
# print(l1)

# print(l1.count(12))


# ls1 = [1, "Ajay", 2, "Ajay", 3, "Ajay", 4, "Ajay", 5, "Ajay"]

# while "Ajay" in ls1:
#     ls1.remove("Ajay")

# # print(ls1)
# a = [1,2,3,4,5,6]
# b = ['a', 'b', 'c', 'd', 'e']

# c = a+b
# print(c)

# for i in range(len(b)):
#     a.append(b[i])
# print(a)

# to do app
# todo_list = []

# while True:
#     choice = input("Enter 'a' to add a task, 'v' to view tasks, 'r' to remove a task, or 'q' to quit: ")
#     match choice:
#         case 'a':
#             task = input("Enter the task: ")
#             todo_list.append(task)
#             print(f"Task '{task}' added.")
#         case 'v':
#             if not todo_list:
#                 print("No tasks in the list.")
#             else:
#                 print("Tasks:")
#                 for i,task in todo_list:
#                     print(f"{i+1}. {task}")
#         case 'r':
#             if not todo_list:
#                 print("No tasks to remove.")
#             else:
#                 task_num = int(input("Enter the task number to remove: "))
#                 if 1 <= task_num <= len(todo_list):
#                     removed_task = todo_list.pop(task_num - 1)
#                     print(f"Task '{removed_task}' removed.")
#                 else:
#                     print("Invalid task number.")
#         case 'q':
#             print("Exiting the to-do app.")
#             break

# import tkinter as tk
# from tkinter import messagebox


# # ----------------------------
# # Functions
# # ----------------------------
# def add_task():
#     task = task_entry.get().strip()

#     if task == "":
#         messagebox.showwarning("Warning", "Please enter a task.")
#         return

#     todo_list.append(task)
#     task_listbox.insert(tk.END, task)
#     task_entry.delete(0, tk.END)


# def remove_task():
#     try:
#         selected = task_listbox.curselection()[0]
#         removed_task = todo_list.pop(selected)
#         task_listbox.delete(selected)
#         messagebox.showinfo("Task Removed", f"'{removed_task}' removed successfully.")
#     except IndexError:
#         messagebox.showwarning("Warning", "Please select a task to remove.")


# def clear_tasks():
#     if not todo_list:
#         messagebox.showinfo("Info", "Task list is already empty.")
#         return

#     confirm = messagebox.askyesno("Confirm", "Do you want to clear all tasks?")

#     if confirm:
#         todo_list.clear()
#         task_listbox.delete(0, tk.END)


# # ----------------------------
# # Main Window
# # ----------------------------
# root = tk.Tk()
# root.title("To-Do List App")
# root.geometry("500x500")
# root.resizable(False, False)

# todo_list = []

# # ----------------------------
# # Title
# # ----------------------------
# title = tk.Label(
#     root,
#     text="📝 To-Do List",
#     font=("Arial", 20, "bold"),
# )
# title.pack(pady=10)

# # ----------------------------
# # Entry Frame
# # ----------------------------
# entry_frame = tk.Frame(root)
# entry_frame.pack(pady=10)

# task_entry = tk.Entry(
#     entry_frame,
#     width=35,
#     font=("Arial", 13)
# )
# task_entry.grid(row=0, column=0, padx=5)

# add_btn = tk.Button(
#     entry_frame,
#     text="Add Task",
#     command=add_task,
#     width=12,
#     bg="green",
#     fg="white"
# )
# add_btn.grid(row=0, column=1)

# # ----------------------------
# # Listbox Frame
# # ----------------------------
# list_frame = tk.Frame(root)
# list_frame.pack(pady=20)

# scrollbar = tk.Scrollbar(list_frame)

# task_listbox = tk.Listbox(
#     list_frame,
#     width=50,
#     height=15,
#     font=("Arial", 12),
#     yscrollcommand=scrollbar.set,
#     selectbackground="#4CAF50"
# )

# scrollbar.config(command=task_listbox.yview)

# task_listbox.pack(side=tk.LEFT)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# # ----------------------------
# # Buttons
# # ----------------------------
# button_frame = tk.Frame(root)
# button_frame.pack(pady=15)

# remove_btn = tk.Button(
#     button_frame,
#     text="Remove Selected",
#     command=remove_task,
#     width=16,
#     bg="red",
#     fg="white"
# )
# remove_btn.grid(row=0, column=0, padx=10)

# clear_btn = tk.Button(
#     button_frame,
#     text="Clear All",
#     command=clear_tasks,
#     width=16,
#     bg="orange",
#     fg="white"
# )
# clear_btn.grid(row=0, column=1, padx=10)

# # ----------------------------
# # Run
# # ----------------------------
# root.mainloop()


import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QListWidget,
    QLineEdit, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class TodoApp(QWidget):

    def __init__(self):
        super().__init__()

        self.tasks = []

        self.setWindowTitle("Modern To-Do List")
        self.resize(700, 550)

        self.setStyleSheet("""
            QWidget{
                background:#1E1E2E;
                color:white;
                font-size:14px;
            }

            QLabel{
                font-size:26px;
                font-weight:bold;
            }

            QLineEdit{
                background:#313244;
                border:2px solid #45475A;
                border-radius:10px;
                padding:10px;
                color:white;
            }

            QListWidget{
                background:#313244;
                border:none;
                border-radius:12px;
                padding:8px;
                font-size:15px;
            }

            QListWidget::item{
                padding:12px;
                margin:4px;
                border-radius:8px;
            }

            QListWidget::item:selected{
                background:#89B4FA;
                color:black;
            }

            QPushButton{
                background:#89B4FA;
                color:black;
                border:none;
                border-radius:10px;
                padding:12px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#74C7EC;
            }

            QPushButton:pressed{
                background:#5A9BD5;
            }
        """)

        self.build_ui()

    def build_ui(self):

        title = QLabel("📝 My To-Do List")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")

        self.task_list = QListWidget()

        add_btn = QPushButton("➕ Add Task")
        remove_btn = QPushButton("🗑 Remove")
        clear_btn = QPushButton("🧹 Clear All")

        add_btn.clicked.connect(self.add_task)
        remove_btn.clicked.connect(self.remove_task)
        clear_btn.clicked.connect(self.clear_tasks)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(add_btn)

        button_layout = QHBoxLayout()
        button_layout.addWidget(remove_btn)
        button_layout.addWidget(clear_btn)

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addLayout(input_layout)
        layout.addSpacing(15)
        layout.addWidget(self.task_list)
        layout.addSpacing(10)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def add_task(self):

        task = self.task_input.text().strip()

        if not task:
            QMessageBox.warning(self, "Warning", "Enter a task first.")
            return

        self.tasks.append(task)
        self.task_list.addItem(task)
        self.task_input.clear()

    def remove_task(self):

        row = self.task_list.currentRow()

        if row == -1:
            QMessageBox.warning(self, "Warning", "Select a task.")
            return

        self.tasks.pop(row)
        self.task_list.takeItem(row)

    def clear_tasks(self):

        if not self.tasks:
            return

        reply = QMessageBox.question(
            self,
            "Confirm",
            "Clear all tasks?"
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.tasks.clear()
            self.task_list.clear()


app = QApplication(sys.argv)

window = TodoApp()
window.show()

sys.exit(app.exec())