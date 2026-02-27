Конфигурация

user nginx Указывает, что Nginx будет работать от пользователя nginx. Этот пользователь должен существовать в системе (или внутри контейнера)

### Проверка конфигурации внутри конйтейнера
nginx -t
#### Перзапуск внутри
docker exec nginx-container nginx -s reload
или nginx -s reload

# Конфигурация
http {
    include /etc/nginx/mime.types; ### Для
    default_type application/octet-stream;

    sendfile on;
    keepalive_timeout 65;

    log_format custom '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent"';

    access_log /var/log/nginx/access.log custom;

    ### Подключаем виртуальный хост
    server {
        listen 80;
        server_name localhost;

        root /usr/share/nginx/html;
        index index.html;

        error_page 404 /404.html;
        location = /404.html {
            root /usr/share/nginx/html;
        }

        location / {
            expires 7d;
            add_header Cache-Control "public";
        }
    }
}

sudo systemctl restart nginx

