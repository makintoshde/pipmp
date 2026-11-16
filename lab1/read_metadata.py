"""
Скрипт для чтения метаданных медиафайлов.
Заполните пропуски согласно вашему варианту.
"""

import os
import sys

import cv2


def read_audio_metadata(file_path):
    """
    Читает метаданные аудиофайла (MP3, WAV).

    :param file_path: путь к файлу
    :return: словарь с метаданными
    """
    #читаем метаданные с помощью mutagen
    metadata = {}

    # TODO: добавить чтение длительности
    # TODO: добавить чтение битрейта (для MP3)
    # TODO: добавить чтение ID3-тегов (исполнитель, альбом, год)

    return metadata


def read_video_metadata(file_path):
    """
    Читает метаданные видеofайла (MP4, MKV).

    :param file_path: путь к файлу
    :return: словарь с метаданными
    """
    #читаем метаданные с помощью OpenCV
    metadata = {}

    # TODO: добавить чтение разрешения
    # TODO: добавить чтение fps
    # TODO: добавить расчёт длительности

    return metadata


def read_image_metadata(file_path):
    """
    Читает метаданные изображения (JPEG, PNG).

    :param file_path: путь к файлу
    :return: словарь с метаданными
    """
    #читаем метаданные с помощью OpenCV
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        raise ValueError("Не удалось прочитать изображение")
    metadata = {}

    # TODO: добавить чтение размера
    height, width = image.shape[:2]
    metadata["Размер, пикселей"] = f"{width}x{height}"
    # TODO: добавить чтение количества каналов
    channels = 1 if image.ndim == 2 else image.shape[2]
    metadata["Количество каналов"] = channels
    metadata["Глубина цвета, бит/канал"] = image.dtype.itemsize * 8
    metadata["Глубина цвета, бит/пиксель"] = image.dtype.itemsize * 8 * channels

    return metadata


def main():
    """Основная функция."""
    #получаем имя файла из аргументов командной строки
    if len(sys.argv) < 2:
        print("Использование: python read_metadata.py <файл>")
        sys.exit(1)

    file_path = sys.argv[1]

    #определяем тип файла по расширению
    extension = os.path.splitext(file_path)[1].lower()
    if extension not in (".png", ".jpg", ".jpeg"):
        print("Поддерживаются только изображения JPEG и PNG")
        sys.exit(1)
    #вызываем соответствующую функцию чтения метаданных
    try:
        metadata = read_image_metadata(file_path)
    except (OSError, ValueError, cv2.error) as error:
        print(f"Ошибка чтения метаданных: {error}")
        sys.exit(1)
    #выводим результат

    print(f"Метаданные для {file_path}:")
    # TODO: вывести все ключи и значения из metadata
    for key, value in metadata.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    main()
