"""
Основное окно приложения.
Заполните пропуски согласно вашему варианту.
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QWidget, QLabel, QSlider, QComboBox
)


class MainWindow(QMainWindow):
    """Главное окно приложения."""

    def __init__(self):
        super().__init__()
        #устанавливаем заголовок окна
        self.setWindowTitle("Выбор фильтра")
        #устанавливаем размеры окна
        self.setGeometry(100, 100, 400, 200)

        self.init_ui()

    def init_ui(self):
        """Инициализация пользовательского интерфейса."""
        #создаём центральный виджет
        central_widget = QWidget()
        #создаём layout (VBox, HBox или Grid)
        layout = QVBoxLayout()

        #создаём необходимые виджеты
        self.combo = QComboBox()
        self.combo.addItems(["Ч/б", "Размытие", "Яркость"])
        self.label = QLabel("Выбранный фильтр: Ч/б")
        #подключаем сигналы к слотам
        self.combo.currentIndexChanged.connect(self.on_combo_select)
        #добавляем виджеты в layout
        layout.addWidget(self.combo)
        layout.addWidget(self.label)

        #устанавливаем layout на центральный виджет
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_button_click(self):
        """Обработчик нажатия кнопки."""
        #обрабатываем нажатие кнопки
        pass

    def on_slider_change(self, value):
        """Обработчик изменения слайдера."""
        #обрабатываем изменение значения
        pass

    def on_combo_select(self, index):
        """Обработчик выбора элемента из списка."""
        #обрабатываем выбор элемента
        self.label.setText(f"Выбранный фильтр: {self.combo.itemText(index)}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
