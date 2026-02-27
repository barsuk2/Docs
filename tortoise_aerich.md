### aerich
pip install aerich
aerich init -t app.db.TORTOISE_ORM
aerich init-db 🔹 Это создаст таблицы и зафиксирует первую миграцию в app/migrations.

aerich downgrade - откат
aerich downgrade --step 3 

aerich history - сосотояние

🔅️при добавление новой модели нужно зарегичтровать ее в app.db.TORTOISE_ORM
и генерить и применить миграцию
✅️ aerich migrate && aerich upgrade 

