/**
 * Модуль управления пользовательским интерфейсом
 * Обрабатывает обновления UI, переключение режимов, показ/скрытие элементов
 * и другие изменения в интерфейсе
 */
import { getElement, toggleClass } from '../utils/dom-utils.js';
import { changeAppLanguage } from '../utils/i18n.js';

/**
 * Обработчик смены языка интерфейса
 */
export function handleInterfaceLangChange(event) {
  const selectedLang = event.target.value;
  const modelMulti = getElement('model-select');
  const modelEn = getElement('model-select-en');

  changeAppLanguage(selectedLang);

  // Меняем селекторы моделей для английского языка
  if (selectedLang === 'en') {
    toggleClass(modelMulti, 'hidden', true);
    toggleClass(modelEn, 'hidden', false);
    modelMulti.disabled = true;
    modelEn.disabled = false;
  } else {
    toggleClass(modelMulti, 'hidden', false);
    toggleClass(modelEn, 'hidden', true);
    modelMulti.disabled = false;
    modelEn.disabled = true;
  }
}
