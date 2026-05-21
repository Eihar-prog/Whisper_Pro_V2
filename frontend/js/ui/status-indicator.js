/**
 * Модуль управления индикатором статуса
 * Обрабатывает обновление статуса приложения (готов, загрузка модели, процесс и т.д.)
 * и визуальное отображение этих состояний
 */

import {
  addClass,
  getElement,
  removeClass,
  setText,
} from '../utils/dom-utils.js';

// Импортируем функцию локализации
import { t } from '../utils/i18n.js';

/**
 * Обновление статуса приложения
 * @param {string} statusType - Тип статуса ('ready', 'loading-model', 'processing')
 * @param {string} message - Сообщение статуса
 * @param {string} subMessage - Подзаголовок статуса
 * @param {string} color - Цвет индикатора
 */
function updateStatus(statusType, message, subMessage, color) {
  const statusInd = getElement('status-indicator');
  const statusText = getElement('status-text');
  const statusSub = getElement('status-subtext');

  // Устанавливаем цвет индикатора
  statusInd.style.backgroundColor = color;

  // Устанавливаем сообщения
  setText(statusText, message);
  setText(statusSub, subMessage);

  // Управляем классами в зависимости от типа статуса
  if (statusType === 'loading') {
    addClass(statusInd, 'status-loading');
    statusText.style.color = '#eab308'; // yellow
  } else {
    removeClass(statusInd, 'status-loading');
    statusText.style.color = '#e2e8f0'; // slate-200
  }
}

/**
 * Установка статуса готовности
 * @param {string} modelName - Название текущей модели
 */
export function setStatusReady(modelName) {
  // Используем шаблонную строку для динамической подстановки имени модели
  const subMessage = `${t('status_model_prefix')}: ${modelName}`;
  updateStatus('ready', t('status_ready'), subMessage, '#22c55e');
}

/**
 * Установка статуса загрузки модели
 */
export function setStatusLoadingModel() {
  updateStatus(
    'loading',
    t('status_loading'),
    t('status_please_wait'),
    '#eab308',
  );
}

/**
 * Установка статуса обработки
 */
export function setStatusProcessing() {
  updateStatus(
    'processing',
    t('status_processing'),
    t('status_please_wait'),
    '#3b82f6',
  );
}
