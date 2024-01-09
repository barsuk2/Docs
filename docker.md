# docker
### images - посмотреть image
>docker images
удалить none имиджы
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
### images - посмотреть контейнеры
>docker ps - активные
>docker ps -a - все
>docker ps -a - l

### собрать имадж
>docker build -t 'flaskdocker' . - ТОЧКА ОБЯЗАТЕЛЬНА

docker ps -aq вывод все и только id
sudo docker cp wwi.bak sql1:/var/opt/mssql/backupdocker rm $(docker ps -aq) -удалить все по id

## запуск конейнера
docker run hello - запуск
docker run --name hello - запуск

docker run --name debian -i -t debian:latest bash или так

docker run flask --rm -p:5000:5000 -проброс порта

docker run -d hello --name hello --rm - запуск в фоне,удалить контейнер после остановки

### отстановить контейнер
>docker stop nostalgic_hoover - nostalgic_hoover - это имя

### docker volume
сисок волумов
>http://172.17.0.2:5000 

### удалить и оствновить все контейеры
docker system prune

создать волум
>docker volume create web

### pull
docker pull busybox - згрузит контейнер с хаба

### dicker-compose
>docker-compose build - собрать
>docker-compose up - запустить
>docker-compose up --build собрать и запустить

docker-compose -f docker-compose.dev.yml f docker-compose.yml up --build - последовательный запуск yaml


sudo docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P '35Bfx140' \
   -Q 'RESTORE FILELISTONLY FROM DISK = "/var/opt/mssql/backup/BD_backup"' \
   | tr -s ' ' | cut -d ' ' -f 1-2
   

  
### запуск шелл в контейере
sudo docker exec -it sql1 "bash" 
sudo docker exec -it sql1 sh

### коприровать в контейнер
sudo docker cp wwi.bak sql1:/var/opt/mssql/backup


docker run -i -t debian /bin/bash- запустить shell использую контейнер debian
docker run -h CONTAINER -i -t debian /bin/bash -зададим имя хоста
docker inspect nifty_hellman - подробна информаци  о контейнере
docker inspect youthful_swanson --format '{{json .NetworkSettings.Networks}}' - вывод куста

docker diff nifty_hellman - сравние, какие папки была изменены в работающем еонтейнере
docker logs nifty_hellman - список всех событий в контейнере
docker ps -aq -f status=exited - спсиок id всех остановленных контейнеров.
### удалить контейнер
docker rm -v $(docker ps -aq -f status=exited) - удалить все контейнеры с по списку ID и их тома

### Удалить image

docker images -q -f dangling=true - получить непоименованные по id
 docker rmi test/coweay-dockerfile:latest
 docker rmi 10fcec6d95c4
 

### docker ps
docker ps -f фильтры
https://docs.docker.com/engine/reference/commandline/ps/
status	Один из created, restarting, running, removing, paused, exited, или

### работаем с redis -p 6379

1. запуск контейрена

docker run -d --name some-redis redis

2. получаем доступ из основной ОС 
docker inspect some-redis - так можно узнать IP
redis-cli -h 172.17.0.2 - если установлен redis на main OS
иначе
docker run --rm -it --link some-redis:r_cli redis bash - линкуемся, запускаем bash
или
docker run --rm -it --link some-redis:r_cli redis redis-cli -h r_cli - 

при сборке можно оключить кеширование 

--no-cash

#### history 
набор уровней docker image можно посмотреть
docker history redis


s - запуск конейнера
docker exec -it redis-server redis-cli  - подключение к контейеру



#### docker image

:alpine - минимальный образ
:slim - усеченные версии стандартных образов

### dockerfile - основные инструкции

ADD - копирут файлы из контекста создания иди удаленныз URL
COPY - для копированимя файлов из контекста создания в ораз
CMD - запускает инструкцию во воремя иницилиализации контейнера
ENTRYPOINT (точка входа) определяет запуск программы  при иницилиализации конейнера
ENV -переменные среды вутри контейнера
EXPOSE (разоблачать) - сообщает контейнеру, что буде прослушиваться порт, порты
FROM - определяет основной образ
RUN запускает инструкцию
VOLUME оюявляет заданный каталог (файл) как том. 
WORKDIR - (pwd) рабочий каталог для всех ADD COPY и т д




### Внешний мир

docker run -d -p 8000:80 nginx - порт что слушает на main OS и куда отправляет

--link conteiner_name:alias

### volume
#### Добавление volume черз коммндную строку
egor@astra-linux:/srv/docer_e$ docker run -it --name contei_test --rm  -v /data debian /bin/bash - создается в корне каталог data. ТАкже он монтируется в main OS
/var/lib/docker/volumes/1661e903b554d7add227ca06e1ab1802bcfc90b0ef1de2f06d325e1f728a9f54/_data
это можно узнать
docker inspect contei_test

#### Добавление volume черз Dockerfile  
FROM ..
VOLUME /data

### docker-compose 
up - запуск все контейнеров из compose файла
build - пересобрать
ps - сщостояие контейнера
logs- выво 
run одноразовый запуск
rm - удалилить все остановленные контейнеры
stop - остановка контейнеров без из остановки
down - останвливает контейер и удаляет.

### bind mount

FROM python:3.10
- при данной конфигурации создается в корне контейнера толоко /app

- запускаем контейнер с волюмом bind mount
- docker run --rm -p 5000:5000 -v "$(pwd)"/app:/app flask_dock
LABEL authors="egor"
RUN pip install Flask
WORKDIR /app

COPY app /app

CMD ["python", "main.py"]

### exec

В работающес конейнере можно выполнить команду
vj,bNfnvj,rpfymcgjhnabny
docker exec dock_comp_nginx_1 ls -al /usr/share/nginx/html

### коприровать из конейнера


### Запуск nginx
docker run --rm -p 8000:80  -v $(pwd):/usr/share/nginx/html nginx - в Dock_Comp лежит html

+### docker-compose
 
+####тесты при запускё
 
+    healthcheck:
+      test: ["CMD", "curl", "http://localhost:5000/"]
+      interval: 20s
+      retries: 5
+      start_period

docker-compose down -v удалить и волумы
### спмсок команд
docker exec -it db_ps psql -U test


### vulums
docker volume create example-volume - создать
docker volume ls --filter="name=ex" - фильтрация

docker volume rm asdasd - удалить том
docker volume inspect dasd - посмотреть инфу, например точку монтирования

### network
docker network ls -спсиок сетей


### logs

docker-compose logs --follow - выводить генерируемы сообщения
docker-compose logs -f api - для приложеия api


-ker# docker
+kerker# docker
 
 ### images - посмотреть image
 >docker images
 
 
 CMD ["python", "main.py"]
 
### exec

 
В работающес конейнере можно выполнить команду

### logs
 
 docker-compose logs --follow - выводить генерируемы сообщения
-
-
+docker-compose top - список запущенных процессов
+docker-compose events -события
+docker-compose config - вывод текущий конфигурации compose
+docker-compose config --services - вывод сервисов
+docker-compose config --volumes - т


### postgresql
#### pgbounser docker
*https://hub.docker.com/r/edoburu/pgbouncer/*

docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres:14 -

docker exec -it some-postgres psql -U postgres

docker run --name habr-pg-13.3 -p 5432:5432 -e POSTGRES_USER=habrpguser -e POSTGRES_PASSWORD=pgpwd4habr -e POSTGRES_DB=habrdb -d postgres:13.3

docker exec -it some-postgres psql -U habrpguser 

*https://habr.com/ru/articles/578744/*
ENV POSTGRES_USER=habrpguser - создает юзера БД в место классического postgresq
ENV POSTGRES_PASSWORD=pgpwd4habr - его пароль
ENV POSTGRES_DB=habrdb - новая БД
DB и USER не работают вместе


### спмсок команд
docker exec -it db_ps psql -U test

18353286e082 mp_kasud_redis_1


#### docker register

sudo docker run -d -p 8989:5000 --restart=always --name registry_8989 registry:2
sudo systemctl restart docker - сохраняет контейер
docker run -d -p 8989:5000 -e REGISTRY_AUTH=htpasswd -e REGISTRY_AUTH_HTPASSWD_REALM=Registry -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/

#### запуск c аворизацией
registry.password -e REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY=/data  -v "$PWD/data:/data" -v "$PWD/auth:/auth"  --restart=always  --name registry_8989 registry:2
