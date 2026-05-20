"""
Файл содержит пути (константы) необходимые для работы приложения
"""

import sys
from pathlib import Path

# Определяем корень проекта.
# Если приложение будет заморожено в .exe (например, через PyInstaller),
# у него появится sys._MEIPASS. Предусмотрим это сразу для надежности.
if getattr(sys, "frozen", False):
    # Путь запущенного .exe файла
    BASE_DIR = Path(sys.executable).parent
else:
    # Обычный запуск скрипта.
    # Считаем от этого файла paths.py: вверх до utils -> до py -> до backend -> корень
    BASE_DIR = Path(__file__).resolve().parents[3]

# Объявляем системные папки проекта
JSON_DIR = BASE_DIR / "backend" / "json"
FFMPEG_DIR = BASE_DIR / "ffmpeg"

# Путь к ffprobe
FFPROBE_PATH = FFMPEG_DIR / "bin" / "ffprobe.exe"

# Путь к json файлу поддерживаемых форматов
SUPPORTED_FORMATS_PATH = JSON_DIR / "supported_formats.json"

# Путь к файлу конфигурации
CONFIG_PATH = JSON_DIR / "config.json"

# Путь к главному html файлу
HTML_FILE_PATH = str(BASE_DIR / "index.html")


# Экспортируем только то, что нужно другим модулям
__all__ = [
    "BASE_DIR",
    "FFPROBE_PATH",
    "HTML_FILE_PATH",
    "SUPPORTED_FORMATS_PATH",
    "CONFIG_PATH",
]
