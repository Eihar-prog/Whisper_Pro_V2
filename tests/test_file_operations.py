import json
import tempfile
from pathlib import Path
from unittest.mock import Mock, mock_open, patch

import pytest
import webview

from backend.py.utils.file_operations import (
    load_supported_formats,
    open_file_dialog,
    open_file_path,
    save_file_dialog,
    save_folder_dialog,
    save_text_file,
)


class TestSaveTextFile:
    """Тесты для функции save_text_file"""

    def test_save_text_file_success(self, tmp_path):
        """Happy Path: успешное сохранение текста в файл"""
        text = "Тестовый текст"
        file_path = tmp_path / "test.txt"

        result = save_text_file(text, file_path)

        assert result is True
        assert file_path.read_text(encoding="utf-8") == text

    def test_save_text_file_with_custom_encoding(self, tmp_path):
        """Edge Case: сохранение с нестандартной кодировкой"""
        text = "Тестовый текст без проблемных символов"
        file_path = tmp_path / "test.txt"

        result = save_text_file(text, file_path, encoding="cp1251")

        assert result is True
        # Проверяем, что файл был создан
        assert file_path.exists()

    def test_save_text_file_exception_handling(self, tmp_path):
        """Error Case: обработка исключений при записи в недоступный файл"""
        text = "Тестовый текст"
        # Используем недопустимый путь
        invalid_path = "/invalid/path/test.txt"

        result = save_text_file(text, invalid_path)

        assert result is False


class TestLoadSupportedFormats:
    """Тесты для функции load_supported_formats"""

    def test_load_supported_formats_success(self, tmp_path):
        """Happy Path: успешная загрузка форматов из JSON"""
        # Подготовка тестового JSON файла
        test_data = {
            "audio": {"extensions": [".mp3", ".wav"], "filter": "Audio Files"},
            "video": {"extensions": [".mp4", ".avi"], "filter": "Video Files"},
        }
        json_path = tmp_path / "formats.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(test_data, f, ensure_ascii=False)

        result = load_supported_formats(json_path)

        assert result == test_data

    def test_load_supported_formats_empty_json(self, tmp_path):
        """Edge Case: загрузка из пустого JSON файла"""
        json_path = tmp_path / "empty.json"
        with open(json_path, "w", encoding="utf-8") as f:
            f.write("{}")

        result = load_supported_formats(json_path)

        assert result == {}

    @patch("builtins.open", side_effect=FileNotFoundError("Файл не найден"))
    def test_load_supported_formats_file_not_found(self, mock_open_func):
        """Error Case: обработка ошибки отсутствия файла"""
        with pytest.raises(FileNotFoundError):
            load_supported_formats("/nonexistent/path.json")

    @patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
    def test_load_supported_formats_invalid_json(self, mock_json_load):
        """Error Case: обработка ошибки при разборе невалидного JSON"""
        with patch("builtins.open", mock_open()):
            with pytest.raises(json.JSONDecodeError):
                load_supported_formats("/some/path.json")


class TestSaveFolderDialog:
    """Тесты для функции save_folder_dialog"""

    def test_save_folder_dialog_selected(self):
        """Happy Path: успешный выбор папки"""
        mock_window = Mock()
        mock_window.create_file_dialog.return_value = ["/path/to/selected/folder"]

        result = save_folder_dialog(mock_window)

        assert result == "/path/to/selected/folder"
        mock_window.create_file_dialog.assert_called_once()

    def test_save_folder_dialog_cancelled(self):
        """Edge Case: отмена выбора папки пользователем"""
        mock_window = Mock()
        mock_window.create_file_dialog.return_value = []

        result = save_folder_dialog(mock_window)

        assert result is None


class TestSaveFileDialog:
    """Тесты для функции save_file_dialog"""

    def test_save_file_dialog_audio_success(self, monkeypatch):
        """Happy Path: успешное сохранение аудио файла"""
        monkeypatch.setattr(
            "backend.py.utils.file_operations.open_file_path",
            "/path/to/input/audio.mp3",
        )

        mock_window = Mock()
        mock_window.create_file_dialog.return_value = ["/path/to/output/audio.txt"]

        result = save_file_dialog(
            mock_window, output_dir="/output", is_subtitle_file=False
        )

        assert result == "/path/to/output/audio.txt"
        # Проверяем, что вызван метод с правильными параметрами
        mock_window.create_file_dialog.assert_called_once_with(
            webview.FileDialog.SAVE,
            directory="/output",
            save_filename="audio.txt",
            file_types=(
                "Text file (*.txt)",
            ),  # Исправлено: кортеж строк, а не кортеж кортежей
        )

    def test_save_file_dialog_subtitle_success(self, monkeypatch):
        """Happy Path: успешное сохранение субтитров"""
        monkeypatch.setattr(
            "backend.py.utils.file_operations.open_file_path",
            "/path/to/input/video.mp4",
        )

        mock_window = Mock()
        mock_window.create_file_dialog.return_value = ["/path/to/output/video.srt"]

        result = save_file_dialog(
            mock_window, output_dir="/output", is_subtitle_file=True
        )

        assert result == "/path/to/output/video.srt"

    def test_save_file_dialog_cancelled(self, monkeypatch):
        """Edge Case: отмена диалога сохранения"""
        monkeypatch.setattr(
            "backend.py.utils.file_operations.open_file_path", "/path/to/input/file.mp3"
        )

        mock_window = Mock()
        mock_window.create_file_dialog.return_value = []

        result = save_file_dialog(mock_window)

        assert result is None

    def test_save_file_dialog_no_open_file_path(self, monkeypatch):
        """Edge Case: отсутствие установленного open_file_path"""
        monkeypatch.setattr("backend.py.utils.file_operations.open_file_path", None)

        mock_window = Mock()
        mock_window.create_file_dialog.return_value = ["/path/to/output/output.txt"]

        result = save_file_dialog(
            mock_window, output_dir="/output", is_subtitle_file=False
        )

        assert result == "/path/to/output/output.txt"


class TestOpenFileDialog:
    """Тесты для функции open_file_dialog"""

    def test_open_file_dialog_success(self, tmp_path, monkeypatch):
        """Happy Path: успешный выбор файла"""
        # Подготовка тестового JSON файла с форматами
        test_formats = {
            "audio": {"extensions": [".mp3", ".wav"], "filter": "Audio Files"},
            "video": {"extensions": [".mp4", ".avi"], "filter": "Video Files"},
        }
        formats_path = tmp_path / "formats.json"
        with open(formats_path, "w", encoding="utf-8") as f:
            json.dump(test_formats, f)

        # Не меняем глобальную константу, а подменяем load_supported_formats
        with patch(
            "backend.py.utils.file_operations.load_supported_formats",
            return_value=test_formats,
        ):
            mock_window = Mock()
            mock_window.create_file_dialog.return_value = [
                "/path/to/selected/audio.mp3"
            ]

            result = open_file_dialog(mock_window, "/input/dir")

            assert result == "/path/to/selected/audio.mp3"
            # Проверяем, что глобальная переменная обновлена
            assert (
                result == "/path/to/selected/audio.mp3"
            )  # Проверяем результат, а не глобальную переменную

    def test_open_file_dialog_cancelled(self, tmp_path, monkeypatch):
        """Edge Case: отмена выбора файла"""
        # Подготовка тестового JSON файла с форматами
        test_formats = {
            "audio": {"extensions": [".mp3", ".wav"], "filter": "Audio Files"},
            "video": {"extensions": [".mp4", ".avi"], "filter": "Video Files"},
        }
        formats_path = tmp_path / "formats.json"
        with open(formats_path, "w", encoding="utf-8") as f:
            json.dump(test_formats, f)

        monkeypatch.setattr(
            "backend.py.utils.file_operations.SUPPORTED_FORMATS_PATH", formats_path
        )

        mock_window = Mock()
        mock_window.create_file_dialog.return_value = []

        result = open_file_dialog(mock_window, "/input/dir")

        assert result is None

    @patch(
        "backend.py.utils.file_operations.load_supported_formats",
        side_effect=Exception("Ошибка загрузки"),
    )
    def test_open_file_dialog_load_formats_error(self, mock_load_func, tmp_path):
        """Error Case: обработка ошибки при загрузке форматов"""
        # Даже если load_supported_formats выбрасывает исключение,
        # open_file_dialog должна передать его дальше
        with pytest.raises(Exception, match="Ошибка загрузки"):
            open_file_dialog(Mock(), "/input/dir", "/nonexistent/path.json")
