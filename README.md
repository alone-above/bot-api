# Alone Above — API Service

FastAPI сервер для Telegram Mini App (index.html).

## Переменные окружения (Railway → Variables)

Те же самые что и в bot-service:

| Переменная | Описание |
|---|---|
| `BOT_TOKEN` | Токен бота (нужен для отправки уведомлений менеджеру) |
| `ADMIN_IDS` | ID администраторов |
| `MANAGER_ID` | ID менеджера для уведомлений о заказах |
| `SUPPORT_USERNAME` | @username поддержки |
| `SHOP_NAME` | Название магазина |
| `KASPI_PHONE` | Номер Kaspi |
| `DATABASE_URL` | PostgreSQL internal URL (Railway) |
| `DATABASE_PUBLIC_URL` | PostgreSQL public URL |
| `CRYPTOBOT_TOKEN` | Токен CryptoBot |

## После деплоя

1. Railway выдаст URL вида `https://alone-above-api-xxxx.up.railway.app`
2. Вставь этот URL в `index.html`:
   ```js
   const BOT_API = 'https://alone-above-api-xxxx.up.railway.app';
   ```
3. Залей обновлённый `index.html` на GitHub Pages

## Запуск

```
web: python run_api.py
```
