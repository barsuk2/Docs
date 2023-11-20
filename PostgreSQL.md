Alembic - построен поверх SQLAlchemy
Умеет автоматически генерировать код миграций.

ОСНОВНЫЕ КОММАНДЫ
alembic upgrade head - накатить все
alembic downgrade -1 - откатить одно
alembic revision --autogenerate -m 'комментарий, поясняющий миграцию' - генерация миграции
alembic revision --autogenerate -m "TeamMember extensions"
alembic current - где находится текущий head. хеш текущей миграции

1. Необходимо проверять откат миграций и дорабатывать их в ручную.
op.create_foreign_key('team_members_city_id_fkey', 'team_members', 'cities', ['city_id'], ['id']) - добавлено имя ключа team_members_city_id_fkey
   
op.execute('DROP TYPE team_member_status_type') - такими образом можно выполнить sql код 

УДАЛЕНИЕ БД ПРИВОДИТ К УДАЛЕНИЮ ВСЕХ МИГРАЦИЙ

### PostgreSQL

##### Подключение к базе
sudo su postgres
psql

\l -  List of databases
\h for help with SQL commands
\? for help with psql commands
\c DBNAME connect to new database (currently "postgres")
\d list tables, views, and sequences




 - удалить базу
sudo -u postgres dropdb mp_base;
- создать БД
sudo -u postgres psql -c "CREATE DATABASE mp_base OWNER mp_owner"

sudo -u postgres psql -c "CREATE USER roompark ENCRYPTED PASSWORD 'roompark'"
sudo -u postgres psql -c "CREATE DATABASE roompark OWNER roompark"



#### UPDATE
op.execute("UPDATE team_members SET _timezone = user._timezone FROM tours WHERE tours.footage_id = footages.id;"
изменить таблицу ,,, установить значение столбцу .... из таблицы .... где столбец = столбцу

### Агрегатные

SELECT users.id, array_agg(team_statuses_1.type) as sad FROM users LEFT OUTER JOIN team_statuses AS team_statuses_1 ON users.id = team_statuses_1.user_id
LEFT OUTER JOIN team_members AS team_members_1 ON users.id = team_members_1.user_id group by users.id;

SELECT users.id, array_agg(team_statuses_1.type) as sad FROM users LEFT OUTER JOIN team_statuses AS team_statuses_1 ON users.id = team_statuses_1.user_id
group by users.id;

SELECT users.id, count(team_statuses_1.type) as sad FROM users LEFT OUTER JOIN team_statuses AS team_statuses_1 ON users.id = team_statuses_1.user_id
group by users.id;

### insert 
https://postgrespro.ru/docs/postgresql/12/sql-insert
INSERT INTO films (code, title, did, date_prod, kind)
    VALUES ('T_601', 'Yojimbo', 106, '1961-06-16', 'Drama'), ('T_601', 'Yojimbo', 106, '1961-06-16', 'Drama');
    
    
#### delete
delete from users where username = 'egor';

### функции генерирующие множества
https://postgrespro.ru/docs/postgresql/9.5/functions-srf
generate_series(start, stop, step или iterval)

>>> select generate_series(1, 10);
>>> select generate_series(1, 10, 6);
>>> select generate_series('2022-01-01':: TIMESTAMP,'2022-01-31', '1 day'); 
>>> generate_series(current_date, '2023-05-31', '1 day');

### LATERAL JOIN
Данная конструкция используется для рабаты с временм

###
операторы и функции даты и времени
https://postgrespro.ru/docs/postgresql/12/functions-datetime

### dump
https://postgrespro.ru/docs/postgrespro/10/backup-dump
## создание
>pg_dump bd_name > /home/dir
## восстановаление
psql имя_базы < файл_дампа