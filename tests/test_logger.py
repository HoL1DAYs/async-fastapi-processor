import os
from app.services.logger import logger, log_file

def test_logger_creates_and_writes_log(tmp_path):
    # Подменяем путь до лог-файла
    test_log_file = tmp_path / "test_app.log"

    # Добавляем временный хендлер
    from logging.handlers import RotatingFileHandler
    from logging import Formatter

    handler = RotatingFileHandler(test_log_file, maxBytes=1_000_000, backupCount=1)
    handler.setFormatter(Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)

    test_message = "This is a test log message"
    logger.info(test_message)

    logger.removeHandler(handler)  # Удаляем тестовый хендлер

    # Проверка, что файл создан
    assert test_log_file.exists()

    # Проверка, что сообщение записано
    content = test_log_file.read_text()
    assert test_message in content

    # Проверка на формат (начинается с даты и уровня логирования)
    assert "INFO" in content
