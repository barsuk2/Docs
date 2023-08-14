/etc/postgresql/9.6/main/postgresql.conf — основной
конфигурационный файл, содержащий значения
параметров сервера;

#### ORM SCUD


#### pagination пагинация 
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/pagination/
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/api/#flask_sqlalchemy.SQLAlchemy.paginate

### ДОбавть

from visul.model import Tour

new_tour = Tour()
new_tour.id=12
db.seesion.add(a)
db.sessio.commmit()

### Удалить
### db.session.delete() удаляет ОДНУ запись

db.session.delete(of_tours)
db.session.commit()
## postgrysql sql

sudo -i -u postgres - запуск шела от имени
sudo -u postgres psql - запуск от имени 

### PSQL HELP

\h- помощь по sql командам
\? помощь по plsql

>>\c БД - коннект к БД
\l -спсиок баз

#### Общее знание

#### Информационные схемы

select * from information_schema.information_schema_catalog_name; - имя БД

select count(*) from information_schema.tables where table_schema = 'public'; - сколько таблиц в схеме public

### ORDER_BY

select * from gallery_images order by 2 ; Сортировка по позиции
select id from gallery_images order by id ; сортировка по полю
select description from gallery_images order by description nulls last  ; - сортировка по полю, значения null после, first - значения null до



### JSON
select id ,meta from footages where meta = '{"a":10}' ; - полное совпадение всего поля

#### Получим содержимое ключа как JSON obj
select id , meta -> 'floors' from footages;
#### Получить вложенные ключи
select id  , meta -> 'floors' -> '1' from footages ;

#### Получим содержимое ключа как text
select id , meta ->> 'floors' from footages;


#### Начинается c  ключ-значение
select id ,meta from footages where meta @> '{"mtl": "models/LP.mtl"}' 



#### Содержит пару ключей
select id ,meta from footages where meta ?& array ['floors','a'];

#### Сравнение
select id ,meta from footages where meta ->> 'a'>'3';
select id ,meta from footages where meta -> 'a'>'5';


## sqlalchemy
### VERSION
.__version__
flask_sqlalchemy.__version__



### ORDER_BY

1 Accessing the field properties asc and dsc:
query.order_by(SpreadsheetCells.y_index.desc()) # desc
query.order_by(SpreadsheetCells.y_index.asc()) # asc

2 Using the asc and desc module functions:

from sqlalchemy import asc, desc

query.order_by(desc(SpreadsheetCells.y_index)) # desc
query.order_by(asc(SpreadsheetCells.y_index)) # asc

### FILTER

session.query(User).filter(User.name == 'Bob')
session.query(User).filter(User.birthday < dt.date(2000, 1, 1))
For the first case, there is a shortcut:

session.query(User).filter_by(name='Bob')

### LIMIT

User.query.limit(1).all()

User.query.filter(User.email.endswith('@example.com')).all() - отфильтовать окнанчиватеся на example.com

Конструкция LIKE
Tour.query.filter(Tour.title.like('Empty%')).first()

from visual.app import create_app
app= create_app('config.local.py')
app.app_context().push()
from visual.core import db
from visual.models import Tour, Footage, User, Folder
like = "%min%"
q= Tour.query.filter(Tour.title.ilike(like)).first()
q



Конструкция IN Вхождение
Tour.query.filter(Tour.footage_id.in_([1,2])

Конструкция ИЛИ Вхождение
result = session.query(Customers).filter(or_(Customers.id>2, Customers.name.like('Ra%'))))


Связь один ко многим удобно реализовывать через систему парных ссылок в моделях. 


JION

user = User.query.get(5).join(TeamMember).outerjoin(TeamMemberStatus, TeamMemberStatus.finish > datatime.datatime.now() )
user = db.session.query(User).join(TeamMember).outerjoin(TeamMemberStatus, TeamMemberStatus.finish > datatime.datatime.now() )

ery = db.session.query(User, TeamMemberStatus, TeamMember).join(TeamMember).outerjoin(TeamMemberStatus)


### DISTINCT - отоборать уникальные

db.session.query(User.created_by).distinct().all()	
db.session.query(Task).distinct(Task.title).all()

### group_by

db.session.query(Task.user_id, Users.username, db.func.count()).join(Users).group_by(Task.user_id, Users.username).all()
db.session.query(Task.user_id, db.func.count()).group_by(Task.user_id).all()
### array_agg

q = db.session.query(User, db.func.array_agg(TeamMemberStatus.id)).join(TeamMember).outerjoin(TeamMemberStatus).group_by(User.id)


q = db.session.query(User,db.func.array_agg(TeamMemberStatus.type)).join(TeamMember).outerjoin(TeamMemberStatus).group_by(User.id)



q = db.session.query(User, cast(db.func.array_agg(db.func.row(TeamMemberStatus.type,'||',TeamMemberStatus.start,'||',TeamMemberStatus.finish)),ARRAY(String))).join(TeamMember).outerjoin(TeamMemberStatus).group_by(User.id)



q = db.session.query(User, db.func.row(db.func.array_agg(TeamMemberStatus.type),db.func.array_agg(TeamMemberStatus.start))).join(TeamMember).outerjoin(TeamMemberStatus).group_by(User.id)


q = db.session.query(User, db.func.array_agg(TeamMemberStatus.query.all())).join(TeamMember).outerjoin(TeamMemberStatus).group_by(User.id)

### json_agg
q1 = db.session.query(User, db.func.json_agg(TeamMemberStatus.id)).join(TeamMember).outerjoin(TeamMemberStatus).group_by(User.id)

#### Вложенные запросы

Вывести имена пользователей, членов команды	

sub = db.session.query(TeamMember.user_id).subquery()

Вывести имена из 1 отдела
dep = db.session.query(TeamMember.user_id,TeamMember.department_id).filter(TeamMember.department_id == 1).subquery('sub')
q= db.session.query(User.name, dep.c.department_id).join(dep, User.id == dep.c.user_id) 

print(sub.c) - посмотреть таблицу




[(<User 9:Строкина Татьяна>, '("{4,5,8,9}","{2019-08-01,2020-08-01,2021-09-01,2022-08-01}","{2019-08-01,2020-08-01,2021-09-01,2022-08-01}")'), (<User 42:kasiatora>, '("{6,7}","{2021-08-01,2019-08-01}","{2021-08-01,2019-08-01}")'), (<User 4:NEWBIE@BIGANTO.COM>, '({NULL},{NULL},{NULL})'), (<User 50:Новый>, '({NULL},{NULL},{NULL})'), (<User 49:qqq>, '({NULL},{NULL},{NULL})'), (<User 40:werwt>, '({NULL},{NULL},{NULL})'), (<User 48:egor ццц>, '({NULL},{NULL},{NULL})'), (<User 47:egor>, '({NULL},{NULL},{NULL})'), (<User 32:eweq123123>, '({NULL},{NULL},{NULL})')]


[(<User 9:Строкина Татьяна>, ['(sick-leave,2019-08-01,2019-08-24)', '(maternity-leave,2020-08-01,2020-08-24)', '(vacation,2021-09-01,2021-09-24)', '(vacation,2022-08-01,2022-08-24)']), (<User 42:kasiatora>, ['(vacation,2021-08-01,2021-08-24)', '(vacation,2019-08-01,2019-08-24)']), (<User 4:NEWBIE@BIGANTO.COM>, ['(,,)']), (<User 50:Новый>, ['(,,)']), (<User 49:qqq>, ['(,,)']), (<User 40:werwt>, ['(,,)']), (<User 48:egor ццц>, ['(,,)']), (<User 47:egor>, ['(,,)']), (<User 32:eweq123123>, ['(,,)'])]



### JSON


q = q.filter(db.or_(Footage.meta['floors']['1'].astext.cast(String).notlike(big_map),
                                Footage.meta['floors']['1'].astext.cast(String).notlike(small_map)))


### realationship ОТНОШЕНИЯ МЕЖДУ ОБЪЕКТАМИ

#### backref
class User()
team_status = db.relationship('TeamMemberStatus', backref='user') 
означает, что по ссылке team_status можем получить объект TeamMemberStatus и из TeamMemberStatus можем получить объект User 

#### back_populates - аналогично backref создает ссылки, однако должны быть пары в каждом объекте
team_status = db.relationship('TeamMemberStatus', back_populates='user')
user = db.relationship('User', back_populates='team_status')



#### фильтр даты
https://stackoverflow.com/questions/51451768/sqlalchemy-querying-with-datetime-columns-to-filter-by-month-day-year

Task.query.filter(extract('month', Task.completed) == 3).all() - извлечь месяц

### is not null is null 
.is(None)
.isnot(None)

#### distinct
.distinct(literal_column('month')) не повотряющиемся по вычисляемого полю

#### подзапросы

t = Session.query(
    Posts.user_id,
    func.max(Posts.post_time).label('max_post_time'),
).group_by(Posts.user_id).subquery('t')

