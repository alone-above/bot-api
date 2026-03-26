# Alone Above Shop — Bot API

## Изменения в этой версии

### Новые поля товара (15 шагов при добавлении)
1. Категория
2. Название
3. Описание
4. Цена (актуальная)
5. **Цена до скидки** (зачёркнутая)
6. **Скидка %**
7. Размеры
8. Остаток
9. **Срок доставки** (например: 3–7 дней)
10. **Гарантия** (дней)
11. **Срок возврата** (дней)
12. Телефон продавца
13. Telegram продавца
14. **Аватар продавца** (фото или "нет" → логотип магазина)
15. Обложка товара (card)
16. **Галерея** (несколько фото по одному → "готово")

### DB миграции (автоматически)
Новые колонки добавляются при старте через `ALTER TABLE IF NOT EXISTS`:
- `original_price`, `discount_percent`
- `delivery_days`, `warranty_days`, `return_days`
- `seller_avatar`

### Новый API endpoint
- `GET /products/{id}/gallery` — возвращает card + все фото галереи

## Запуск

```bash
cp .env.example .env   # или создайте .env вручную
pip install -r requirements.txt

# Бот
python main.py

# API (отдельно)
python run_api.py
```

## .env переменные

```
BOT_TOKEN=...
ADMIN_IDS=123456789
MANAGER_ID=123456789
SHOP_NAME=Alone Above Shop
SUPPORT_USERNAME=@support
KASPI_PHONE=+77001234567
DATABASE_URL=postgresql://...
```
