/**
 * Модуль для хранения и изменения локализации приложения (надписи на элементах)
 */

// Текущий язык приложения по умолчанию
let currentLang = 'ru';

export const translations = {
  ru: {
    app_description: 'Инструмент расшифровки аудио на базе ИИ',
    status_ready: 'Готов к работе',
    status_model_prefix: 'Модель',
    status_loading: 'Загрузка модели...',
    status_processing: 'Обработка...',
    status_please_wait: 'Пожалуйста, подождите',
    model_settings_title: 'Настройки модели',
    whisper_model_label: 'Модель Whisper',
    select_model_placeholder: 'Выберите модель...',
    source_lang_label: 'Язык аудио',
    lang_auto: 'Автоопределение',
    lang_en: 'Английский',
    lang_uk: 'Украинский',
    lang_ru: 'Русский',
    lang_de: 'Немецкий',
    lang_es: 'Испанский',
    lang_fr: 'Французский',
    lang_pl: 'Польский',
    translate_toggle_label: 'Мгновенный перевод в EN',
    translate_toggle_desc:
      'Диктуйте на любом языке — Whisper выдаст текст сразу на английском.',
    hotkey_label: 'Горячая клавиша записи',
    hotkey_placeholder: "Нажмите 'Изменить' для установки комбинации",
    btn_change: 'Сменить',
    work_mode_title: 'Режим работы',
    mode_mic_title: 'Голосовой набор',
    mode_mic_desc: 'Вставка текста под курсор',
    mode_file_title: 'Транскрибация файла',
    mode_file_desc: 'Обработка аудиозаписей',
    btn_select_file: 'Выбрать аудиофайл',
    file_not_selected: 'Файл не выбран',
    file_details_empty: 'Длительность: 00:00 | Размер: 0 MB',
    result_label: 'Результат',
    subtitles_label: 'Субтитры (.srt)',
    timestamps_label: 'Таймкоды',
    speakers_label: 'Спикеры',
    btn_copy: 'Копировать',
    btn_save: 'Сохранить',
    settings_gear_title: 'Настройки сохранения',
    pyannote_title: 'Настройки pyannote',
    btn_edit: '📝 Ред.',
    hf_token_label: 'Hugging Face Token',
    pyannote_model_label: 'Модель pyannote',
    min_speakers_label: 'Мин. спикеров',
    max_speakers_label: 'Макс. спикеров',
    folder_label: '📂 Папка:',
    folder_original: 'В папке оригинала',
    folder_select_placeholder: 'Выбрать папку...',
    output_placeholder: 'Здесь появится текст после обработки...',
    progress_title: 'Процесс обработки',
    btn_cancel: '✕ Отмена',
    btn_start: 'Начать транскрибацию',
    no_hotkey: 'Не назначена',
  },
  uk: {
    app_description: 'Інструмент розшифровки аудіо на базі ШІ',
    status_ready: 'Готовий до роботи',
    status_model_prefix: 'Модель',
    status_loading: 'Завантаження моделі...',
    status_processing: 'Обробка...',
    status_please_wait: 'Будь ласка, зачекайте',
    model_settings_title: 'Налаштування моделі',
    whisper_model_label: 'Модель Whisper',
    select_model_placeholder: 'Оберіть модель...',
    source_lang_label: 'Мова аудіо',
    lang_auto: 'Автовизначення',
    lang_en: 'Англійська',
    lang_uk: 'Українська',
    lang_ru: 'Російська',
    lang_de: 'Німецька',
    lang_es: 'Іспанська',
    lang_fr: 'Французька',
    lang_pl: 'Польська',
    translate_toggle_label: 'Миттєвий переклад в EN',
    translate_toggle_desc:
      'Диктуйте будь-якою мовою — Whisper видасть текст одразу англійською.',
    hotkey_label: 'Гаряча клавіша запису',
    hotkey_placeholder: "Натисніть 'Змінити' для встановлення комбінації",
    btn_change: 'Змінити',
    work_mode_title: 'Режим роботи',
    mode_mic_title: 'Голосове введення',
    mode_mic_desc: 'Вставка тексту під курсор',
    mode_file_title: 'Транскрибація файлу',
    mode_file_desc: 'Обробка аудіозаписів',
    btn_select_file: 'Обрати аудіофайл',
    file_not_selected: 'Файл не обрано',
    file_details_empty: 'Тривалість: 00:00 | Розмір: 0 MB',
    result_label: 'Результат',
    subtitles_label: 'Субтитри (.srt)',
    timestamps_label: 'Таймкоди',
    speakers_label: 'Спікери',
    btn_copy: 'Копіювати',
    btn_save: 'Зберегти',
    settings_gear_title: 'Налаштування збереження',
    pyannote_title: 'Налаштування pyannote',
    btn_edit: '📝 Ред.',
    hf_token_label: 'Hugging Face Token',
    pyannote_model_label: 'Модель pyannote',
    min_speakers_label: 'Мін. спікерів',
    max_speakers_label: 'Макс. спікерів',
    folder_label: '📂 Папка:',
    folder_original: 'У папці оригіналу',
    folder_select_placeholder: 'Обрати папку...',
    output_placeholder: "Тут з'явиться текст після обробки...",
    progress_title: 'Процес обробки',
    btn_cancel: '✕ Скасувати',
    btn_start: 'Почати транскрибацію',
    no_hotkey: 'Не призначена',
  },
  en: {
    app_description: 'AI-powered audio transcription tool',
    status_ready: 'Ready',
    status_model_prefix: 'Model',
    status_loading: 'Loading model...',
    status_processing: 'Processing...',
    status_please_wait: 'Please wait',
    model_settings_title: 'Model Settings',
    whisper_model_label: 'Whisper Model',
    select_model_placeholder: 'Select model...',
    source_lang_label: 'Audio language',
    lang_auto: 'Auto Detect',
    lang_en: 'English',
    lang_uk: 'Ukrainian',
    lang_ru: 'Russian',
    lang_de: 'German',
    lang_es: 'Spanish',
    lang_fr: 'French',
    lang_pl: 'Polish',
    translate_toggle_label: 'Instant Translate to EN',
    translate_toggle_desc:
      'Dictate in any language — Whisper will output text directly in English.',
    hotkey_label: 'Recording Hotkey',
    hotkey_placeholder: "Click 'Change' to set a combination",
    btn_change: 'Change',
    work_mode_title: 'Operation Mode',
    mode_mic_title: 'Voice Typing',
    mode_mic_desc: 'Insert text under cursor',
    mode_file_title: 'File Transcription',
    mode_file_desc: 'Audio file processing',
    btn_select_file: 'Select Audio File',
    file_not_selected: 'No file selected',
    file_details_empty: 'Duration: 00:00 | Size: 0 MB',
    result_label: 'Result',
    subtitles_label: 'Subtitles (.srt)',
    timestamps_label: 'Timestamps',
    speakers_label: 'Speakers',
    btn_copy: 'Copy',
    btn_save: 'Save',
    settings_gear_title: 'Save settings',
    pyannote_title: 'Pyannote Settings',
    btn_edit: '📝 Edit',
    hf_token_label: 'Hugging Face Token',
    pyannote_model_label: 'Pyannote Model',
    min_speakers_label: 'Min Speakers',
    max_speakers_label: 'Max Speakers',
    folder_label: '📂 Folder:',
    folder_original: 'In original folder',
    folder_select_placeholder: 'Choose folder...',
    output_placeholder: 'The text will appear here after processing...',
    progress_title: 'Processing',
    btn_cancel: '✕ Cancel',
    btn_start: 'Start Transcription',
    no_hotkey: 'Not assigned',
  },
};

/**
 * Получить перевод по ключу для текущего языка
 */
export function t(key) {
  return translations[currentLang]?.[key] || key;
}

/**
 * Автоматически переводит все элементы на форме, у которых есть data-i18n атрибуты
 * @param {string} lang - 'ru', 'uk' или 'en'
 */
export function changeAppLanguage(lang) {
  if (!translations[lang]) return;
  currentLang = lang;

  // 1. Переводим обычный текст внутри элементов
  const textElements = document.querySelectorAll('[data-i18n]');
  textElements.forEach((el) => {
    const key = el.dataset.i18n;
    const translation = t(key);

    // Если внутри элемента есть иконки или структура (например, радиокнопки со span внутри),
    // нужно аккуратно менять только текстовый узел. Но для простых блоков меняем textContent.
    if (el.children.length === 0) {
      el.textContent = translation;
    } else {
      // Если внутри есть структура, ищем именно текстовый узел и меняем его,
      // либо переводим только конкретные текстовые дочерние элементы.
      // Для твоей верстки большинство элементов с data-i18n будут чистыми текстовыми тегами.
    }
  });

  // 2. Переводим плейсхолдеры (placeholder) инпутов и textarea
  const placeholderElements = document.querySelectorAll(
    '[data-i18n-placeholder]',
  );
  placeholderElements.forEach((el) => {
    const key = el.getAttribute('data-i18n-placeholder');
    el.placeholder = t(key);
  });

  // 3. Переводим всплывающие подсказки (title)
  const titleElements = document.querySelectorAll('[data-i18n-title]');
  titleElements.forEach((el) => {
    const key = el.getAttribute('data-i18n-title');
    el.title = t(key);
  });

  // 4. Ручное обновление динамического статуса, если элементы есть на странице
  const statusTextEl = document.getElementById('status-text');
  const statusSubEl = document.getElementById('status-subtext');

  if (statusTextEl && statusSubEl) {
    // Нам нужно понять, какое состояние сейчас активно, чтобы правильно перевести.
    // Самый простой способ — проверить текущий текст или цвет, но еще лучше
    // ориентироваться на сохраненное состояние, либо просто перезаписать тексты:

    if (
      statusTextEl.textContent === translations.ru.status_ready ||
      statusTextEl.textContent === translations.uk.status_ready ||
      statusTextEl.textContent === translations.en.status_ready
    ) {
      statusTextEl.textContent = t('status_ready');
      // Вытаскиваем имя модели, которое шло после двоеточия
      const currentModel = statusSubEl.textContent.split(': ')[1] || 'Base';
      statusSubEl.textContent = `${t('status_model_prefix')}: ${currentModel}`;
    } else if (
      statusTextEl.textContent.includes('Загрузка') ||
      statusTextEl.textContent.includes('Завантаження') ||
      statusTextEl.textContent.includes('Loading')
    ) {
      statusTextEl.textContent = t('status_loading');
      statusSubEl.textContent = t('status_please_wait');
    } else {
      statusTextEl.textContent = t('status_processing');
      statusSubEl.textContent = t('status_please_wait');
    }
  }

  // Сохраняем выбранный язык в общий конфиг приложения на бэкенд, чтобы он запоминался
  if (window.pywebview && pywebview.api) {
    pywebview.api.set_setting('app_language', lang);
    pywebview.api.save_config();
  }
}
