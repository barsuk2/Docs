Отправка писем из Python используя модуль smtplib
https://selenium-python.com/smtplib-email-example

Как настроить доступ к Gmail в сторонних почтовых клиентах
https://support.google.com/mail/answer/7126229?hl=ru#zippy=%2Cшаг-измените-smtp-и-другие-параметры-в-клиенте

Активируйте разрешение на использование небезопасных приложений. После этого дополнително подтвердить действие в разделе безопасность.

### Локальный сервер-эмуляция почтовой доставки 
python -m smtpd -c DebuggingServer -n localhost:1025


#### Насатройка отправки чЕрез gmail
config.local.py
MAIL_ENABLED = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_TLS = True
MAIL_USER = 'e.mihajlov@gmail.com'
MAIL_PASSWORD = '6oisxI20wHEZ'

#### Использование терминала для тестирования 

with app.test_request_context():
    send_email(
        gettext('Tour "%(title)s" successfully created', title=(tour.title if tour.title else gettext('Untitled'))),
        [tour.user.email],
        'no-reply@biganto.com',
        template='mail/build_success',
        tour=tour
    )
    
