# docker
### images - посмотреть image
>docker images
удалить none имиджы
>docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
### images - посмотреть контейнеры
>docker ps - активные
>docker ps -a - все
>docker ps -a - l

### собрать имадж
>docker build -t 'flaskdocker' . -

docker ps -aq вывод все и только id
sudo docker cp wwi.bak sql1:/var/opt/mssql/backupdocker rm $(docker ps -aq) -удалить все по id

## запуск конейнера
docker run hello - запуск
docker run --name hello - запуск
docker run --name deb -i -t debian:latest bash или так
docker run flask --rm -p:5000:5000 -проброс порта

docker run -d hello --name hello --rm - запуск в фоне,удалить контейнер после остановки

### отстановить контейнер
>docker stop nostalgic_hoover - nostalgic_hoover -имя

### docker volume
сисок волумов
>http://172.17.0.2:5000 

создать волум
>docker volume create web

### pull
docker pull busybox - згрузит контейнер с хаба

### dicker-compose
>docker-compose build - собрать
>docker-compose up - запустить
>docker-compose up --build собрать и запустить

docker-compose -f docker-compose.dev.yml f docker-compose.yml up --build - последовательный запуск yaml


sudo docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd -S localhost \
   -U SA -P '35Bfx140' \
   -Q 'RESTORE FILELISTONLY FROM DISK = "/var/opt/mssql/backup/BD_backup"' \
   | tr -s ' ' | cut -d ' ' -f 1-2
   

  
### запуск шелл в контейере
sudo docker exec -it sql1 "bash" 

### коприровать в контейнер
sudo docker cp wwi.bak sql1:/var/opt/mssql/backup

docker run -i -t debian /bin/bash- запустить shell использую контейнер debian
docker run -h CONTAINER -i -t debian /bin/bash -зададим имя хоста
docker inspect nifty_hellman - подробна информаци  о контейнере
docker diff nifty_hellman - сравние, какие папки была изменены в работающем еонтейнере
docker logs nifty_hellman - список всех событий в контейнере
docker ps -aq -f status=exited - спсиок id всех остановленных контейнеров.
### удалить контейнер
docker rm -v $(docker ps -aq -f status=exited) - удалить все контейнеры с по списку ID

### Удалить image

docker images -f dangling=true - получить непоименованные
 docker rmi test/coweay-dockerfile:latest
 docker rmi 10fcec6d95c4
 

### docker ps
docker ps -f фильтры
https://docs.docker.com/engine/reference/commandline/ps/
status	Один из created, restarting, running, removing, paused, exited, или

### запуск redmy    redis



s - запуск конейнера
docker exec -it redis-server redis-cli  - подключение к контейеру
