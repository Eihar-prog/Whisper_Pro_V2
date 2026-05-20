import json
import tempfile
from pathlib import Path
from unittest.mock import mock_open, patch

from backend.py.utils.config import ConfigManager


def test_config_file_not_exists(tmp_path):
    """Тестирует поведение при отсутствии файла конфига - должен быть создан файл с дефолтными значениями"""
    # Создаем временный путь для конфига
    temp_config_path = tmp_path / "config.json"

    # Создаем экземпляр ConfigManager и заменяем путь к конфигу
    config_manager = ConfigManager()
    config_manager.config_path = temp_config_path

    # Загружаем конфиг (файл не существует)
    result = config_manager.load(
        reset=True
    )  # Используем reset=True для перезаписи пути

    # Проверяем, что возвращаются дефолтные значения
    assert result == config_manager.defaults

    # Проверяем, что файл был создан и содержит дефолтные значения
    assert temp_config_path.exists()
    with open(temp_config_path, "r", encoding="utf-8") as f:
        saved_data = json.load(f)
    assert saved_data == config_manager.defaults


def test_config_file_valid_json(tmp_path):
    """Тестирует загрузку конфига из корректного JSON файла"""
    # Подготовим тестовые данные
    valid_config_data = {
        "model_size": "large",
        "source_language": "ru",
        "translate_to_english": True,
        "hotkey_record": "alt+f1",
    }

    # Создаем временный файл с данными
    temp_config_path = tmp_path / "config.json"
    with open(temp_config_path, "w", encoding="utf-8") as f:
        json.dump(valid_config_data, f, indent=4, ensure_ascii=False)

    # Создаем экземпляр ConfigManager и заменяем путь к конфигу
    config_manager = ConfigManager()
    config_manager.config_path = temp_config_path

    # Загружаем конфиг
    result = config_manager.load()

    # Проверяем, что данные корректно загрузились
    # Данные должны содержать как наши значения, так и дефолтные
    expected_result = {**config_manager.defaults, **valid_config_data}
    assert result == expected_result


def test_config_partial_settings(tmp_path):
    """Тестирует загрузку частичных настроек - остальные должны заполняться из дефолтов"""
    # Подготовим частичные данные
    partial_data = {"model_size": "medium", "source_language": "en"}

    # Создаем временный файл с частичными данными
    temp_config_path = tmp_path / "config.json"
    with open(temp_config_path, "w", encoding="utf-8") as f:
        json.dump(partial_data, f, indent=4, ensure_ascii=False)

    # Создаем экземпляр ConfigManager и заменяем путь к конфигу
    config_manager = ConfigManager()
    config_manager.config_path = temp_config_path

    # Загружаем конфиг
    result = config_manager.load()

    # Проверяем, что установленные значения перезаписали дефолтные
    assert result["model_size"] == "medium"
    assert result["source_language"] == "en"

    # Проверяем, что другие значения остались дефолтными
    assert (
        result["translate_to_english"]
        == config_manager.defaults["translate_to_english"]
    )
    assert result["hotkey_record"] == config_manager.defaults["hotkey_record"]


def test_config_invalid_json(tmp_path):
    """Тестирует поведение при невалидном JSON - должен вернуть дефолтные настройки"""
    # Создаем файл с невалидным JSON
    temp_config_path = tmp_path / "config.json"
    with open(temp_config_path, "w", encoding="utf-8") as f:
        f.write("{ invalid json content")

    # Создаем экземпляр ConfigManager и заменяем путь к конфигу
    config_manager = ConfigManager()
    config_manager.config_path = temp_config_path

    # Загружаем конфиг - должна сработать обработка исключения
    result = config_manager.load()

    # Проверяем, что возвращаются дефолтные значения
    assert result == config_manager.defaults


def test_get_set_save_methods(tmp_path):
    """Тестирует работу методов get(), set() и save()"""
    # Создаем временный путь для конфига
    temp_config_path = tmp_path / "config.json"

    # Создаем экземпляр ConfigManager и заменяем путь к конфигу
    config_manager = ConfigManager()
    config_manager.config_path = temp_config_path

    # Проверяем начальное значение через get()
    initial_value = config_manager.get("model_size")
    assert initial_value == config_manager.defaults["model_size"]

    # Устанавливаем новое значение через set()
    new_value = "test_model"
    config_manager.set("model_size", new_value)

    # Проверяем, что значение изменилось
    assert config_manager.get("model_size") == new_value

    # Сохраняем изменения
    config_manager.save()

    # Проверяем, что изменения сохранились в файле
    assert temp_config_path.exists()
    with open(temp_config_path, "r", encoding="utf-8") as f:
        saved_data = json.load(f)
    assert saved_data["model_size"] == new_value

    # Загружаем конфиг заново и проверяем значение
    reloaded_config_manager = ConfigManager()
    reloaded_config_manager.config_path = temp_config_path
    reloaded_data = reloaded_config_manager.load()
    assert reloaded_data["model_size"] == new_value


def test_get_all_configs(tmp_path):
    """Тестирует метод get_all(), проверяя, что возвращается полный словарь настроек"""
    # Создаем временный путь для конфига
    temp_config_path = tmp_path / "config.json"

    # Создаем экземпляр ConfigManager и заменяем путь к конфигу
    config_manager = ConfigManager()
    config_manager.config_path = temp_config_path

    # Вызываем метод явно
    all_settings = config_manager.get_all()

    # Проверяем, что вернулся словарь и в нем есть дефолтный ключ
    assert isinstance(all_settings, dict)
    assert "model_size" in all_settings
    # Проверяем, что полученные настройки совпадают с текущими данными менеджера
    assert all_settings == config_manager.data


def test_config_reset_existing_file(tmp_path):
    """Тестирует принудительный сброс настроек (reset=True), когда файл уже существует"""
    temp_config_path = tmp_path / "config.json"

    # 1. Сначала создаем файл с какими-то измененными настройками
    custom_data = {"model_size": "large", "source_language": "ru"}
    config_manager = ConfigManager()
    config_manager.config_path = temp_config_path
    config_manager.save(custom_data)

    # 2. Вызываем load с reset=True. Это должно зайти в блок else и вызвать принт
    result = config_manager.load(reset=True)

    # 3. Проверяем, что настройки сбросились до дефолтных, несмотря на существовавший файл
    assert result == config_manager.defaults


def test_config_save_exception(tmp_path):
    """Тестирует перехват исключения в методе save(), если запись в файл невозможна"""
    temp_config_path = tmp_path / "config.json"
    config_manager = ConfigManager()
    config_manager.config_path = temp_config_path

    # Используем встроенный контекстный менеджер patch для безопасной подмены.
    # Мы говорим: "Только на время этого блока builtins.open будет вызывать ошибку"
    with patch("builtins.open", mock_open()) as mocked_file:
        # Заставляем наш искусственный open выбрасывать исключение при вызове
        mocked_file.side_effect = IOError("Ошибка записи на диск")

        # Пытаемся сохранить. Код наткнется на ошибку, уйдет в except и сделает принт.
        config_manager.save()

    # Тест успешно пройдет, так как класс обработал ошибку внутри себя,
    # а patch автоматически вернул оригинальный open на место сразу после выхода из блока с with.
