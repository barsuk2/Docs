Деплой dev-окружения
Каждый разработчик поднимает у себя весь движок сайта biganto.com. Движок работает под linux.
Мастдайным юзерам рекомендуется виртуалка с Arch или Debian. WSL не прокатит. Оконный менеджер (GUI) в этой виртуалке будет только жрать память и рекомендуется к установке только слабым духом разработчикам.
Этот мануал написан исходя из предположений:


Репозиторий склонирован в /srv/biganto.com (по умолчанию репозиторий клонируется как папка visual, ее нужно переименовать в biganto.com и положить в /srv). На эту директорию указывают
дефолтные значения большинства директив конфигурации. Если репозиторий склонирован в какое-нибудь другое место, то, помимо
путей в этом мануале, нужно переопределить все константы с этими путями из config.py в config.local.py.
У вас linux и вы умеете с ним работать.
Вы разобрались, что такое виртуальное окружение python и научились работать с
virtualenvwrapper.


1. Ставим системные пакеты

Для Debian:
$ sudo apt-get install nginx git postgresql python3 python3-dev virtualenvwrapper npm cpp make cmake redis libxt6 libxrender1 libxcomposite1
В остальных системах ищите соотетствия имён пакетов в репозиториях самостоятельно.

2. Рабочие директории

Создаём директории, которых нет в репозитории (и они помещены в .gitignore):
$ mkdir -p /srv/biganto.com/bin
$ mkdir -p /srv/biganto.com/var/assets
$ mkdir -p /srv/biganto.com/var/flow-upload
$ mkdir -p /srv/biganto.com/var/logs
$ mkdir -p /srv/biganto.com/var/purgatory/footages
В /srv/biganto.com/var будут лежать логи и ассеты системы, и их может быть довольно много. Если на том разделе, где
находится /srv/biganto.com/ недостаточно места, создайте директорию var и её поддиректории в свободном разделе и симлинк на неё
(ln -s /mnt/hugeHDD/biganto.com/var /srv/biganto.com/var).

3. Создаём виртуальное окружение python и ставим в него пакеты

Нам нужен питон не ниже версии 3.7.
$ mkvirtualenv -p `which python3` biganto_com
(если не работает mkvirtualenv смотри тут)
$ pip install -r requirements.txt

4. Создаём visual/config.local.py

Это конфиг, где можно преопределить любые константы основного конфига, visual/config.py. Запишите туда следующее:
SQLALCHEMY_DATABASE_URI = 'postgresql://visual:writecleancode@localhost:5432/visual'
MAIL_ENABLED = False
MAIL_SINK = ('newbie@biganto.com',) # Пропишите сюда ваш адрес почты
Если боитесь перепутать админку на проде и админку дев-окружения, то в visual/config.local.py можно задать фон админки инстанса движка:
ADMIN_BGCOLOR = '#0DEAD0'

5. Создаём и инициализируем базу данных

$ sudo -u postgres psql -c "CREATE USER visual ENCRYPTED PASSWORD 'writecleancode'"
$ sudo -u postgres psql -c "CREATE DATABASE visual OWNER visual"
$ alembic upgrade head

6. Скачиваем и устанавливаем внешние утилиты
Этот шаг можно пропустить, если вы не собираетесь собирать туры или редактировать их модели немедленно, однако его всё
равно нужно сделать, чтобы не дебажить потом полдня, почему не работает сборка туров в личном кабинете и не получить за это по жопе.
Движок иногда запускает внешние программы, которых нет в общедоступных системных пакетах. Все они живут в /srv/biganto.com/bin:


metro. Качаем и ставим .deb-пакет.

MatLabRuntime. Скачиваем его отсюда,
разворачиваем zip во временную директорию и запускаем:
$ ./install -mode silent -agreeToLicense yes -destinationFolder /srv/biganto.com/bin/MLR


nizpodoh. Скачиваем его отсюда, разворачиваем в
/srv/biganto.com/bin/nizpodoh. После этого редактируем /srv/biganto.com/bin/nizpodoh/nizpodoh.cfg: в директиве path_python
нужно прописать путь к интерпретатору  python того virtualenv'а, под которым у вас работает дев-окружение. Его можно узнать командой
which python, работая под этим виртуальным окружением. Переход в виртуальное окружение делается командой
workon biganto_com


calc_passways. Бинарник тут, кладём в bin.
Пользователям Arch linux, возможно, понадобится библиотека libxcrypt-compat, если низподох падает с соответствующим сообщением.

Все бинарники собраны под архитектуру x86_64. Если у вас другая — пересобирать замучаетесь.

7. Собираем фронтэнд
Понадобится nodejs версии 16.14 и npm 8.5.
Если у вас не та версия, то рекомендуется использовать системный пакет nvm
Установка nvm и node и npm через nvm
sudo apt install curl -y 
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
source ~/.bashrc

nvm install 16.14.0
nvm alias default 16.14.0
nvm use default
npm install -g npm@8.5.0
cd /srv/biganto.com & find . -name 'node_modules' -type d -prune -print -exec rm -rf '{}' \;
./buildfrontend.sh
Если npm ругнётся на неверную версию npm (в выводе будет что-то типа Required: {"node":"~16.14.0","npm":"~8.5.0"} Actual: {"npm":"8.3.1","node":"v16.14.0"}), то нужную версию можно поставить командой
npm install -g npm@8.5.0

8. Настраиваем nginx
Приложение движка сайта (которое мы в конце запустим скриптом runserver.sh) само по себе является HTTP-сервером и
слушает порт 5000. Однако, чтобы отдавать контент из var/assets и работать в условиях, приближённых к боевым, нужно настроить
в nginx виртуальный хост:
server {
    server_name local.biganto.com localhost;
    error_log /srv/biganto.com/var/logs/nginx.err.log;
    client_max_body_size 256M;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        root /srv/biganto.com/visual;
        try_files $uri $uri/ =404;
    }

    location /assets {
        root /srv/biganto.com/var;
        try_files $uri $uri/ =404;
    }
    gzip_types text/plain text/css application/json application/x-javascript application/javascript text/xml application/xml application/xml+rss text/javascript image/svg+xml;
}

9. Регаем себя
В базе данных сайта сейчас нет никаких юзеров. Чтобы локально пользоваться локальной админкой и заливать туда туры, нужно
создать пользователя с суперправами (подставьте вашу почту и придумайте крутой пароль; программсты, пользующиеся паролями
типа qwerty123 после смерти попадают в 1С.):
$ ./py.py team-member-create super newbie@biganto.com YourPassword 
После этого можно логиниться на локальный сайт. Для работы есть смысл скопировать в локальное окружение несколько туров с продакшена.
Для этого создаёте своему пользователю папку в личном кабинете (потому что пока туров без папок не бывает), зайдите в админку
боевого сервера и в разделе "Туры" в свойствах любого тура нажмите кнопку "Скачать в ZIP". Затем в уже локальной админке (НЕ ПЕРЕПУТАЙТЕ!)
найдите в разделе "Объекты" в ваш объект, нажмите "Туры (0)" и там кнопку "Создать тур".
Если во время работы вам нужно собирать туры в личном кабинете, то нужно держать запущенным из директории /srv/biganto.com
менеджер очереди задач: rq worker. Проще всего запустить его в отдельном терминале, но вы можете демонизировать его при помощи
screen или systemd.

Запуск движка и дальнейшая жизнь
В локальном dev-окружении движок запускается из под виртуального окружения biganto_com командой .runserver.sh. Если всё прошло
хорошо, можно проверить работу локального движка, открыв в браузере http://local.biganto.com/. Если при
запуске движка произошли ошибки, нужно их внимательно прочитать, подумать, ещё раз подумать, перечитать мануал по установке, подумать
ещё раз, и если ничего из этого не помогло, то прийти в чат biganto.dev жаловаться.
В процессе работы, после того, как вы забрали коммит, нужно будет повторять некоторые шаги установки.

Если прилетели файлы в alembic/versions, значит, изменилась структура БД. Нужно запустить alembic upgrade head.
Если прилетело что-то в static/public/ ­ пересобираем фронт ./buildfrontend.sh Сборка осуществляется на базе node (16.14.0). (Для управления версиями node рекомендуется использовать NVM.)
Изменился requirements.txt — обновляем пакеты pip install -r requirements.txt

Изменились файлы в visual/translations — обновляем базу переводов pybabel compile -d visual/translations
