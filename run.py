"""
Точка входа в приложение Whisper Pro
Инициализирует pywebview и запускает веб-интерфейс
"""

import sys
from io import TextIOWrapper
from typing import cast

import webview

from backend.py.api.app_api import AppAPI
from backend.py.utils.paths import HTML_FILE_PATH

# Установка UTF-8 для корректного вывода кириллицы в консоль Windows.
cast(TextIOWrapper, sys.stdout).reconfigure(encoding="utf-8")


def setup_webview(api: AppAPI) -> webview.Window:  # Передаем api внутрь
    """Настройка параметров окна pywebview"""
    window = webview.create_window(
        title="Whisper Pro",
        url=HTML_FILE_PATH,
        width=1200,
        height=825,
        min_size=(950, 825),
        background_color="#0F172A",
        confirm_close=False,
        js_api=api,  # Передаем API красиво и официально здесь!
    )

    if window is None:
        raise RuntimeError("Не удалось инициализировать окно pywebview")

    return window


def main():
    """Основная функция запуска приложения"""
    api = AppAPI()
    window = setup_webview(api)  # Передаем api в функцию
    api.set_window(window)

    window.events.closing += api.save_config
    webview.start(debug=False)


if __name__ == "__main__":
    main()
