/**
 * Главный файл приложения Whisper Pro
 * Управляет инициализацией всего приложения, обработкой событий DOMContentLoaded
 * и координацией между различными модулями
 */

import { handleInterfaceLangChange } from './ui/ui-manager.js';
import { getElement } from './utils/dom-utils.js';

// Документ готов к взаимодействию
document.addEventListener('DOMContentLoaded', () => {
  window.addEventListener('pywebviewready', () => {
    InitializeEventListeners();
  });
});

/**
 * Инициализация обработчиков событий
 */
function InitializeEventListeners() {
  // Смена языка приложения
  getElement('interface-language-select').addEventListener(
    'change',
    handleInterfaceLangChange,
  );
}
