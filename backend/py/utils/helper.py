"""
Вспомогательные методы
"""


# Форматирование duration (секунды) в удобном виде
def format_duration(seconds: int) -> str:
    """Превращает секунды в 00:00 или 00:00:00"""
    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)

    if hrs > 0:
        return f"{hrs:02}:{mins:02}:{secs:02}"
    return f"{mins:02}:{secs:02}"


# Форматирует размер файла в удобном виде
def format_size(size_bytes: int) -> str:
    """Превращает байты в МБ или ГБ"""
    if size_bytes == 0:
        return "0 Б"

    # Делим на 1024^2 для МБ
    size_mb = size_bytes / (1024 * 1024)

    if size_mb < 1024:
        return f"{size_mb:.2f} МБ"

    # Если вдруг файл больше гигабайта
    size_gb = size_mb / 1024
    return f"{size_gb:.2f} ГБ"


def add_srt_numeration(text: str) -> str:
    """Превращает сырые таймкоды в нумерованные блоки SRT"""
    blocks = text.split("\n\n")
    # Добавим strip для самих блоков, чтобы пустые строки не дублировались
    numbered_blocks = [
        f"{i+1}\n{block.strip()}" for i, block in enumerate(blocks) if block.strip()
    ]
    return "\n\n".join(numbered_blocks)
