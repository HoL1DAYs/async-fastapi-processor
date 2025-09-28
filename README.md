# Async FastAPI Processor

Асинхронный микросервис на FastAPI, который:
- Принимает произвольный JSON через REST API
- Выполняет внешний HTTP-запрос к https://catfact.ninja/fact
- Возвращает объединённый ответ клиенту
- Сохраняет историю запросов в Redis
- Ведёт логирование всех запросов и ответов в файл

---

# Запуск проекта

Собрать и запустить контейнеры:

docker-compose up --build

---

# Запуск тестов:

docker-compose run --rm app pytest

Можно запускать отдельные тесты:

docker-compose run --rm app pytest tests/test_process.py -v

docker-compose run --rm app pytest tests/test_logger.py -v

---

# Команды работы с Redis

Открыть Redis CLI:

docker exec -it async-fastapi-processor-redis-1 redis-cli

Получить список ключей:
keys *

Посмотреть содержимое по UUID:
get <uuid>

Пример:
get f41254e9-2c63-496d-8d95-c928c14c0690

---
Все HTTP-запросы и ответы логируются в файл:
logs/app.log
