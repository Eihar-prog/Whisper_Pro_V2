from unittest.mock import MagicMock, patch

import pytest
import webview

import run


def test_setup_webview_success():
    """Тестирует успешное создание окна pywebview"""
    mock_api = MagicMock()
    mock_window = MagicMock(spec=webview.Window)

    # Подменяем реальное создание окна на возврат нашей заглушки
    with patch("webview.create_window", return_value=mock_window) as mock_create:
        window = run.setup_webview(mock_api)

        # Проверяем, что функция вернула окно и вызвала создание с нужными параметрами
        assert window == mock_window
        mock_create.assert_called_once()


def test_setup_webview_none_exception():
    """Тестирует выброс RuntimeError, если движок не смог создать окно (вернул None)"""
    mock_api = MagicMock()

    # Имитируем ситуацию, когда операционная система вернула None вместо окна
    with patch("webview.create_window", return_value=None):
        with pytest.raises(
            RuntimeError, match="Не удалось инициализировать окно pywebview"
        ):
            run.setup_webview(mock_api)


def test_main_execution():
    """Тестирует основную функцию main без реального открытия окна приложения"""
    # Создаем базовый mock для окна
    mock_window = MagicMock()

    # Имитируем структуру window.events.closing, чтобы прибавление += не падало
    mock_closing_event = MagicMock()
    mock_window.events.closing = mock_closing_event

    # Явно указываем полный путь импорта класса AppAPI внутри модуля run,
    # а также изолируем запуск webview
    with patch("run.AppAPI") as mock_api_class, patch(
        "run.setup_webview", return_value=mock_window
    ) as mock_setup, patch("run.webview.start") as mock_start:

        # Создаем заглушку для инстанса API, чтобы методы set_window и save_config не падали
        mock_api_instance = MagicMock()
        mock_api_class.return_value = mock_api_instance

        # Запускаем main
        run.main()

        # Проверяем корректность вызовов
        mock_api_class.assert_called_once()
        mock_setup.assert_called_once()
        mock_start.assert_called_once_with(debug=False)
