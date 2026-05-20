"""
Вспомогательные функции для работы с файлами
Сохранение, чтение, форматирование
"""

import json
import subprocess
from pathlib import Path

import webview

from backend.py.utils.paths import SUPPORTED_FORMATS_PATH

# Путь к открытому файлу
open_file_path = None


# Сохранение текста в файл
def save_text_file(text, file_path, encoding="utf-8"):
    """Сохранить текст в файл"""
    try:
        with open(file_path, "w", encoding=encoding) as f:
            f.write(text)
        print(f"✅ Файл сохранён: {file_path}")
        return True
    except Exception as e:
        print(f"❌ Ошибка при сохранении: {e}")
        return False


# Диалог выбора папки для сохранения
def save_folder_dialog(window: webview.Window) -> str | None:
    """Открывает диалог выбора папки для сохранения"""
    folder = window.create_file_dialog(webview.FileDialog.FOLDER)
    return folder[0] if folder else None


#  Диалог сохранения файла
def save_file_dialog(
    window: webview.Window, output_dir="/", is_subtitle_file=False
) -> str | None:
    """Открыть диалог сохранения файла"""

    file_name_only = Path(open_file_path).stem if open_file_path else "output"

    result = window.create_file_dialog(
        webview.FileDialog.SAVE,
        directory=output_dir,
        save_filename=(
            f"{file_name_only}.srt" if is_subtitle_file else f"{file_name_only}.txt"
        ),
        file_types=(
            ("SubRip Subtitle (*.srt)",) if is_subtitle_file else ("Text file (*.txt)",)
        ),
    )

    if result:
        save_path = result[0]
        print(f"Saved to {save_path}")
        return save_path

    print("User cancelled save dialog")
    return None


# Загрузка поддерживаемых форматов
def load_supported_formats(json_path: Path | str) -> dict:
    """Загрузить поддерживаемые форматы из JSON файла"""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


# Диалог выбора файла
def open_file_dialog(
    window: webview.Window, input_dir: str, formats_json_path=SUPPORTED_FORMATS_PATH
) -> str | None:
    """Открыть диалог выбора файла с фильтрацией из JSON"""
    formats = load_supported_formats(formats_json_path)

    # Создаем маски
    audio_extensions = formats["audio"]["extensions"]
    video_extensions = formats["video"]["extensions"]

    audio_mask = ";".join(f"*{ext}" for ext in audio_extensions)
    video_mask = ";".join(f"*{ext}" for ext in video_extensions)

    audio_filter_name = formats["audio"]["filter"]
    video_filter_name = formats["video"]["filter"]

    # ПРАВИЛЬНЫЙ ФОРМАТ: описание и маска вместе в одной строке
    file_types = [
        f"{audio_filter_name} ({audio_mask})",
        f"{video_filter_name} ({video_mask})",
        "All files (*.*)",
    ]

    file_path_tuple = window.create_file_dialog(
        webview.FileDialog.OPEN,
        directory=input_dir,
        allow_multiple=False,
        file_types=file_types,
    )
    if file_path_tuple:
        global open_file_path
        open_file_path = file_path_tuple[0]
        return open_file_path
    return None
