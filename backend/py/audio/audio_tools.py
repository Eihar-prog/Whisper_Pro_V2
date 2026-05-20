"""
Модуль обработки аудио данных
"""

import json
import subprocess

from backend.py.utils.paths import FFPROBE_PATH


#  Получение метаданных аудио или видео файла
def get_file_metadata(file_path: str) -> tuple[int, int]:
    """Получить метаданные аудиофайла (длительность, размер)"""
    # parents[2] — это три уровня вверх от файла со скриптом
    ffprobe_path = FFPROBE_PATH

    cmd = [
        str(ffprobe_path),
        "-v",
        "error",
        "-show_entries",
        "format=duration,size",  # Убрали select_streams для универсальности
        "-of",
        "json",
        file_path,
    ]

    # capture_output=True автоматически разделит stdout и stderr
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    if result.returncode != 0:
        raise RuntimeError(f"FFprobe error: {result.stderr}")

    data = json.loads(result.stdout)

    # Используем .get() на случай, если файл странный и какое-то поле отсутствует
    duration_seconds = int(float(data.get("format", {}).get("duration", 0)))
    size_bytes = int(data.get("format", {}).get("size", 0))

    return duration_seconds, size_bytes
