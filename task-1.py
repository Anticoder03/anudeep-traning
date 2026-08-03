import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QLineEdit,
    QMessageBox,
    QInputDialog,
)
from PyQt6.QtCore import Qt


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.tasks = []

        self.setWindowTitle("📝 Modern To-Do List")
        self.resize(750, 600)

        self.setStyleSheet("""
            QWidget{
                background:#1E1E2E;
                color:white;
                font-size:14px;
                font-family:Segoe UI;
            }

            QLabel{
                font-size:28px;
                font-weight:bold;
                color:#FFFFFF;
            }

            QLineEdit{
                background:#313244;
                border:2px solid #45475A;
                border-radius:10px;
                padding:10px;
                color:white;
                font-size:15px;
            }

            QLineEdit:focus{
                border:2px solid #89B4FA;
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
                font-size:14px;
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
        self.task_input.returnPressed.connect(self.add_task)

        self.task_list = QListWidget()

        # Double-click to edit
        self.task_list.itemDoubleClicked.connect(
            lambda: self.edit_task()
        )

        add_btn = QPushButton("➕ Add Task")
        edit_btn = QPushButton("✏️ Edit Task")
        remove_btn = QPushButton("🗑 Remove")
        clear_btn = QPushButton("🧹 Clear All")

        add_btn.clicked.connect(self.add_task)
        edit_btn.clicked.connect(self.edit_task)
        remove_btn.clicked.connect(self.remove_task)
        clear_btn.clicked.connect(self.clear_tasks)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(add_btn)

        button_layout = QHBoxLayout()
        button_layout.addWidget(edit_btn)
        button_layout.addWidget(remove_btn)
        button_layout.addWidget(clear_btn)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title)
        main_layout.addSpacing(15)
        main_layout.addLayout(input_layout)
        main_layout.addSpacing(15)
        main_layout.addWidget(self.task_list)
        main_layout.addSpacing(10)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    # -------------------------
    # Add Task
    # -------------------------
    def add_task(self):
        task = self.task_input.text().strip()

        if not task:
            QMessageBox.warning(
                self,
                "Warning",
                "Please enter a task."
            )
            return

        self.tasks.append(task)
        self.task_list.addItem(task)
        self.task_input.clear()
        self.task_input.setFocus()

    # -------------------------
    # Edit Task
    # -------------------------
    def edit_task(self):
        row = self.task_list.currentRow()

        if row == -1:
            QMessageBox.warning(
                self,
                "Warning",
                "Please select a task to edit."
            )
            return

        current_task = self.tasks[row]

        new_task, ok = QInputDialog.getText(
            self,
            "Edit Task",
            "Update your task:",
            text=current_task,
        )

        if ok:
            new_task = new_task.strip()

            if not new_task:
                QMessageBox.warning(
                    self,
                    "Warning",
                    "Task cannot be empty."
                )
                return

            self.tasks[row] = new_task
            self.task_list.item(row).setText(new_task)

    # -------------------------
    # Remove Task
    # -------------------------
    def remove_task(self):
        row = self.task_list.currentRow()

        if row == -1:
            QMessageBox.warning(
                self,
                "Warning",
                "Please select a task."
            )
            return

        task = self.tasks[row]

        reply = QMessageBox.question(
            self,
            "Remove Task",
            f"Delete '{task}'?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.tasks.pop(row)
            self.task_list.takeItem(row)

    # -------------------------
    # Clear All Tasks
    # -------------------------
    def clear_tasks(self):
        if not self.tasks:
            QMessageBox.information(
                self,
                "Info",
                "Task list is already empty."
            )
            return

        reply = QMessageBox.question(
            self,
            "Clear All",
            "Are you sure you want to delete all tasks?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.tasks.clear()
            self.task_list.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TodoApp()
    window.show()

    sys.exit(app.exec())