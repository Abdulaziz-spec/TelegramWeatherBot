# TelegramWeatherBot

**TelegramWeatherBot** — это Telegram-бот, который предоставляет пользователю информацию о погоде в любом городе, а также справочную информацию о странах и поиск по Википедии. Проект написан на Python и использует популярные библиотеки для работы с Telegram, HTTP-запросами и обработки данных.

## Возможности

- Получение актуальной погоды по названию города (используется OpenWeatherMap API).
- Просмотр информации о странах (столица, население, площадь и т.д.).
- Поиск информации по Википедии прямо в Telegram.
- Простой интерфейс с кнопками для быстрого доступа к функциям.

## Используемые библиотеки

- **pyTelegramBotAPI (telebot)** — для работы с Telegram Bot API.
- **requests** — для отправки HTTP-запросов к внешним API.
- **wikipedia** — для поиска и вывода информации из Википедии.
- **countryinfo** — для получения данных о странах.
- **datetime** — стандартная библиотека Python для работы с датой и временем.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Abdulaziz-spec/TelegramWeatherBot.git
   cd TelegramWeatherBot
   ```

2. Установите зависимости:
   ```bash
   pip install pyTelegramBotAPI requests wikipedia countryinfo
   ```

3. Получите API-ключ для OpenWeatherMap на [openweathermap.org](https://openweathermap.org/api).

4. В файле `main.py` и/или `func_bot.py` замените строки с `'your-token'` и `'your-api'` на ваши ключи:
   ```python
   TOKEN = 'ваш_telegram_token'
   parameters = {
       'appid': 'ваш_openweathermap_api_key',
       'units': 'metric',
       'lang': 'ru'
   }
   ```

5. Запустите бота:
   ```bash
   python main.py
   ```

## Пример использования

- Введите `/start` — для начала работы с ботом.
- Выберите нужную функцию с помощью кнопок.
- Следуйте инструкциям бота для получения информации о погоде, стране или поиска по Википедии.

## Структура проекта

```
TelegramWeatherBot/
├── main.py        # Основная логика бота и обработка команд
├── func_bot.py    # Функции получения погоды и информации о странах
├── buttons.py     # Кнопки для меню
├── venv/          # Виртуальное окружение (опционально)
└── README.md      # Документация
```

## Лицензия

Проект распространяется под лицензией MIT.

---

**TelegramWeatherBot** — ваш информатор о погоде и странах в Telegram!
