"""
Скрипт для конвертации медиафайлов с помощью FFmpeg.
Заполните пропуски согласно вашему варианту.
"""

import subprocess
import shutil
import sys


def check_ffmpeg():
    """Проверяет наличие FFmpeg в системе."""
    #проверяем наличие FFmpeg с помощью shutil.which()
    # Если FFmpeg не найден, выведите сообщение и завершите работу

    if shutil.which("ffmpeg") is None:
        print("FFmpeg не найден в системе")
        sys.exit(1)


def convert_file(input_path, output_path):
    """
    Конвертирует медиафайл с помощью FFmpeg.

    :param input_path: путь к исходному файлу
    :param output_path: путь к выходному файлу
    :return: True при успехе, False при ошибке
    """
    #формируем команду FFmpeg
    command = ["ffmpeg", "-y", "-i", input_path, "-frames:v", "1", output_path]
    #запускаем subprocess.run()
    try:
        result = subprocess.run(command, capture_output=True, text=True)
    except OSError as error:
        print(f"Ошибка запуска FFmpeg: {error}")
        return False
    #проверяем код возврата
    if result.returncode != 0:
        print(f"Ошибка FFmpeg: {result.stderr}")
        return False

    return True


def main():
    """Основная функция."""
    if len(sys.argv) < 3:
        print("Использование: python convert_media.py <входной_файл> <выходной_файл>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    #проверяем наличие FFmpeg
    check_ffmpeg()
    #запускаем конвертацию
    if not input_path.lower().endswith(".png") or not output_path.lower().endswith((".jpg", ".jpeg")):
        print("Для варианта 3 используется конвертация PNG → JPEG")
        sys.exit(1)
    if not convert_file(input_path, output_path):
        sys.exit(1)
    #выводим результат

    print("Конвертация завершена")


if __name__ == '__main__':
    main()
