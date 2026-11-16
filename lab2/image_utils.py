"""
Утилиты для работы с изображениями.
"""

import cv2
from PyQt6.QtGui import QPixmap, QImage


def load_image(file_path):
    """
    Загружает изображение из файла.

    :param file_path: путь к файлу изображения
    :return: изображение в формате OpenCV (NumPy array) или None
    """
    #загружаем изображение с помощью cv2.imread()
    #проверяем, что файл существует и читается
    pass


def opencv_to_qt_image(cv_image):
    """
    Преобразует изображение из OpenCV в QPixmap.

    :param cv_image: изображение в формате OpenCV (NumPy array)
    :return: QPixmap для отображения в Qt
    """
    #преобразуем BGR в RGB
    #создаём QImage из NumPy array
    #возвращаем QPixmap

    pass


def display_image(label, cv_image):
    """
    Отображает изображение в QLabel.

    :param label: QLabel для отображения
    :param cv_image: изображение в формате OpenCV
    """
    #преобразуем изображение
    #устанавливаем pixmap на label
    pass
