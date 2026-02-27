ACK = acknowledge (подтверждаю)
Handshake — это просто «рукопожатие»

проверим 443 порт
nc -vz google.com 443

# Главная команда DevOps #👑️
openssl s_client -connect google.com:443 -servername google.com
openssl s_client -connect mobappkasud-dev.nornik.ru:443 -servername mobappkasud-dev.nornik.ru


### у меня должен быть pivate.key -это моя личность, моя печать
openssl genrsa -out private.key 2048


### дальше я должен создать ЗАПРОС НА ИЗГОТОВЛЕНИЕ СЕРТИФИКАТА CSR (Certificate Signing Request)
openssl req -new -key private.key -out request.csr
### Посмотреть что внутри запроса
openssl req -in request.csr -noout -text

Запомнить одной фразой

🤯️CSR — это заявление:
«Я владею этим доменом, вот мой публичный ключ, подпишите меня»


### Сейчас мы сами будем «центром сертификации» 😄

(для локалки / dev / теста — идеально)

команда
openssl x509 -req -in request.csr -signkey private.key -days 365 -out cert.pem

#### посмотерть созданный серт
openssl x509 -in cert.pem -text -noout

#### 💥проверяем, что ключ и cert совпадают


openssl rsa  -noout -modulus -in private.key | openssl md5
openssl x509 -noout -modulus -in cert.pem     | openssl md5

#### Проверяем что отдает ПРОД снаружи и внутри 
##### Провенряем sha
###### внешний
openssl s_client -connect 91.209.147.79:443 -servername mobappkasud-prod.nornik.ru | openssl x509 -noout -subject -issuer -dates -fingerprint -sha256
> 2F:6F:07:10:C6:3F:16:7C:D2:47:9E:81:8A:D7:B8:C4:C6:E2:1D:12:04:69:4C:E6:12:3E:24:8B:22:4F:F9:5A
###### внутрен
openssl x509 -in /path/to/fullchain.crt -noout -subject -issuer -dates -fingerprint -sha256
#### Проверяем serial
openssl s_client -connect 91.209.147.79:443 -servername mobappkasud-dev.nornik.ru | openssl x509 -noout -serial 

###### внутрен
openssl x509 -in cert.pem -noout -serial

openssl s_client -connect 91.209.147.79:443 -servername mobappkasud-preprod.nornik.ru | openssl x509 -noout -subject -issuer -dates
openssl s_client -connect 91.209.147.79:443 -servername mobappkasud-dev.nornik.ru | openssl x509 -noout -subject -issuer -dates
openssl s_client -connect 91.209.147.79:443 -servername mobappkasud-test.nornik.ru | openssl x509 -noout -subject -issuer -dates

#### Проверяем что отдает chain

openssl x509 -in /path/to/fullchain.crt -noout -subject -issuer -dates -fingerprint -sha256


























