service mysql status - проверка статуса службы
service mysql stop - остановка службы
service mysql start - остановка службы
top - аналог диспетчера задач. Управление запущенным задачами.
ps aux | grep mysql - поиск процесса по имени утилитой ps и grep

### Свободное место на диске 
https://itproffi.ru/analiz-diskovogo-prostranstva-v-linux-komandy-du-i-ncdu/
>sudo du --max-depth=1 -h /home/egor/
ИЛИ
>ncdu

> Работа с дисками
fdisk
https://disnetern.ru/add-new-hdd-ubuntu/

https://losst.ru/perenos-linux-na-drugoj-disk - перенести на другой диск

setsid gedit - запуск в теневом режиме

#### grub
https://losst.ru/nastrojka-zagruzchika-grub
sudo grub-install /dev/sdb - инсталлfuser

sudo update-grub2 - пересобрать меню загрузки

### Изменить права на файл

chmod ugo+x mscript.sh -добавим "исполняемость" для юзера, группы, и прочих 

#### sudo su
su postgres - заменть оболочку от postgres
 
### юзеры группы

#### юзеры

id  [egor] - все о юзере
chage -l egor - истечении срока действия пароля пользователя.


cat /etc/passwd - все пользователи
getent passwd - более удобный аналог
getent passwd {1000..60000} - не системные пользователи
users [user]- список груп юзера linux

#### группы
getent group - список всех групп
getent passwd user_2 - инфомауци о юзере из passwd
adduser name- добавитьи в режиме диалога
useradd new_group - добавить юзера без всего
su admin - заменяет оболочку (bash) на указаную

sudo usermod admin -aG astra-admin -  добавть пользователя admin в группу astra-admin
#### добавить пароль
passwd admin
passwd [user] - сменить парол текущему юзеру или user

### Изменение пользователей
Для того, чтобы изменить параметры уже существующей учетной записи используется команда usermod, 
usermod -h

#### удалить юзера
userdel admin
* конец блок юзер




#### nc - NetCat аналог telnet


### службы и сервисы

sudo systemctl list-units --type service
sudo service redis-server status


service nginx stop

### сокеты
https://zalinux.ru/?p=3193
ss список


### сетевые дела

Кто работает на заданном порту
sudo netstat -pna | grep 6379

-### apt установленные пакеты
-apt list --installed

### bash
#### for цикл
https://andreyex.ru/linux/bash-dlya-tsikla-v-odnoj-stroke/
for i in {1..5}; do echo "number:$i"; sleep 1; done
### awk - один из самых мощных инструментов для обработки и фильтрации текста
https://losst.pro/ispolzovanie-awk-v-linux
echo 'one two three four' | awk '{print $1}'
>one

#### запуск команд с интервалом 
watch -n 1 ll




