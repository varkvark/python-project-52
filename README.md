### Hexlet tests and linter status:
[![Actions Status](https://github.com/varkvark/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/varkvark/python-project-52/actions)
[![hexlet-check](https://github.com/varkvark/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/varkvark/python-project-52/actions/workflows/hexlet-check.yml)


# Task Manager

**Демо:** [https://python-project-52-dh79.onrender.com](https://python-project-52-dh79.onrender.com)

## Быстрый старт

### Установка
```bash
# 1. Клонировать репозиторий
git clone https://github.com/varkvark/python-project-52.git
cd python-project-52

# 2. Настроить окружение
cp .env_sample .env  # отредактируйте .env

# 3. Установить зависимости
make install
make migrate
```

### Запуск
```bash
# Разработка
make start-server

# Доступ по адресу: http://localhost:8000
```

## Особенности

- **Регистрация и авторизация** пользователей
- **Управление задачами** (CRUD)
- **Метки и статусы** для задач
- **Фильтрация** по меткам, исполнителю, статусу
- **Адаптивный дизайн** (Bootstrap 5)

## Технологии 🛠️

- Python 3.13+
- Django 6.0+
- PostgreSQL / SQLite
- Bootstrap 5
- Gunicorn

## Основные команды 🔧

```bash
make install      # Установить зависимости
make start-server # Запустить сервер
make test         # Запустить тесты
make lint         # Проверить код
make migrate      # Применить миграции
```
