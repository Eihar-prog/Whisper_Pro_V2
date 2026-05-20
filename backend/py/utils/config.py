import json
import os
from pathlib import Path
from typing import Any

from backend.py.utils.paths import CONFIG_PATH


class ConfigManager:
    def __init__(self):
        """Инициализация менеджера настроек"""
        # Определяем путь к файлу конфиг относительно этого скрипта
        self.config_path = CONFIG_PATH

        # Дефолтные настройки (на случай, если файла нет или он битый)
        self.defaults = {
            "model_size": "",
            "source_language": "auto",
            "translate_to_english": False,
            "hotkey_record": "ctrl+shift+space",
            "operation_mode": "file",
            "audio_input_dir": "",
            "text_output_dir": "",
            "generate_subtitles": True,
            "include_timestamps": False,
            "enable_speaker_diarization": False,
            "pyannote_token": "",
            "pyannote_model": "pyannote/speaker-diarization-3.1",
            "pyannote_min_speakers": "",
            "pyannote_max_speakers": "",
        }
        self.data = self.load()

    # Загрузка настроек
    def load(self, reset=False) -> dict:
        """Загружает конфиг из файла или возвращает дефолт"""
        is_exists = os.path.exists(self.config_path)

        if not is_exists or reset:
            if not is_exists:
                print("Config file not found. Creating default...")
            else:
                print("Reset to default settings...")
            self.save(self.defaults)
            return self.defaults.copy()

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
                # Объединяем с дефолтом, чтобы не потерять новые ключи в будущем
                return {**self.defaults, **loaded_data}
        except (json.JSONDecodeError, Exception) as e:
            print(f"Error loading config: {e}. Using defaults.")
            return self.defaults.copy()

    # Сохранение настроек
    def save(self, data=None) -> bool:
        """Сохранить настройки в файл"""
        # Сохранить файл, если он был изменен
        if data is None:
            data = self.data

        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print("Config saved successfully.")
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

    #  Получение нужной настройки по ключу
    def get(self, key, default=None) -> Any:
        """Получить значение настройки"""
        return self.data.get(key, default)

    #  Получение всех настроек
    def get_all(self) -> dict:
        """Получить все настройки"""
        return self.data

    #  Установка настройки
    def set(self, key, value):
        """Установить значение настройки"""
        self.data[key] = value
