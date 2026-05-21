/**
 * Модуль настроек приложения
 * Хранит и управляет настройками пользователя (язык, горячие клавиши,
 * выбранная модель, параметры интерфейса и т.д.)
 */

/**
 * Сбор настроек UI элементов в объект config
 */
export function collectConfigFromUI() {
  const config = {};
  const elements = document.querySelectorAll('[data-config]');

  elements.forEach((el) => {
    const key = el.dataset.config;

    if (el.type === 'checkbox') {
      config[key] = el.checked;
    } else if (el.type === 'radio') {
      if (el.checked) config[key] = el.value;
    } else if (!el.type || el.tagName === 'SPAN') {
      const text = el.textContent.trim();
      config[key] = text === 'Выбрать папку...' ? '' : text;
    } else {
      config[key] = el.value;
    }
  });

  return config;
}
