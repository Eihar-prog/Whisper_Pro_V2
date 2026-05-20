"""
API точки для взаимодействия с веб-интерфейсом
Обрабатывает вызовы из JavaScript через pywebview
"""

from typing import Any, Optional

import webview

from backend.py.utils.config import ConfigManager


class AppAPI:
    def __init__(self):
        """Инициализация API сервисов"""
        self._window: Optional[webview.Window] = None
        self.config_manager = ConfigManager()

    def set_window(self, window: webview.Window) -> None:
        """Установка ссылки на окно pywebview для диалогов и событий"""
        self._window = window

    # ---------------------------------------------------------------
    # --- Методы работы с конфигурацией ---
    # ---------------------------------------------------------------

    def load_config(self, reset=False) -> dict[str, Any]:
        """Возвращает все текущие настройки приложения"""
        if reset:
            return self.config_manager.load(reset=True)
        return self.config_manager.get_all()

    def set_setting(self, key: str, value: Any) -> bool:
        """Устанавливает конкретный параметр в памяти"""
        try:
            self.config_manager.set(key, value)
            return True
        except Exception:
            return False

    def save_config(self) -> bool:
        """Физически записывает настройки из памяти в config.json"""
        return self.config_manager.save()
