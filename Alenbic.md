Alembic - построен поверх SQLAlchemy
Умеет автоматически генерировать код миграций.

ОСНОВНЫЕ КОММАНДЫ
alembic upgrade head - накатить все
alembic downgrade -1 - откатить одно
alembic revision --autogenerate -m 'comment' - генерация миграции
alembic revision --autogenerate -m "TeamMember extensions"
alembic current - где находится текущий head. хеш текущей миграции

1. Необходимо проверять откат миграций и дорабатывать их в ручную.
op.create_foreign_key('team_members_city_id_fkey', 'team_members', 'cities', ['city_id'], ['id']) - добавлено имя ключа team_members_city_id_fkey
   
op.execute('DROP TYPE team_member_status_type') - такими образом можно выполнить sql код 

УДАЛЕНИЕ БД ПРИВОДИТ К УДАЛЕНИЮ ВСЕХ МИГРАЦИЙ


#### Установка alembic
### Создание среды

alembic init alembic 

