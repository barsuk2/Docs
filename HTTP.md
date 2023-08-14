status_code
200 - ОК
308 - PERMANENT REDIRECT

### http запросы

#### модуль request

#### Простой GET
import requests as RQ
req = RQ.get('https://biganto.com')

req.status_code - ответ сервера
resp.headers - заголовки


GET
B_URL='http://local.biganto.com'
API_QS = {'client': 'web', 'client_version': '1.0'}
API_TOURS =API_QS.copy()
API_TOURS['user_id']=9
rv = requests.get(f'{B_URL}/api/v3/tours', params=API_TOURS)
rv = requests.get(f'{B_URL}/api/v3/tours', params={'client': 'web', 'client_version': '1.0','user_id': '9'})

tours_rv = sess.get(f'{B_URL}/api/v3/tours', params={'client': 'web', 'client_version': '1.0','user_id':9})

### AUTH 🇦🇪️
import requests
B_URL='http://local.biganto.com'
API_QS = {'client': 'web', 'client_version': '1.0'}
API_TOURS =API_QS.copy()
user = requests.post(f'{B_URL}/api/v3/users/login', json={'email': 'kasiatora@ya.ru', 'password': '123'}, params=API_QS)
API_TOURS['auth_token'] = user.json()['result'].get('token')
rv = requests.get(f'{B_URL}/api/v3/tours/81/qr', params=API_TOURS)
### некторые API
Поучить свойство одного тура 
rv = requests.get(f'{B_URL}/api/v3/tours/303', params=API_TOURS)
Получить  QR тура
rv = requests.get(f'{B_URL}/api/v3/tours/303/qr', params=API_TOURS)
Изменить данный пользователя
rv = requests.put(f'{B_URL}/api/v3/users/9', json = {'email': 'kasiatora@yandex.ru'}, params=API_TOURS)

B_URL='https://biganto.com'
user = requests.post(f'{B_URL}/api/v3/users/login', json={'email': 'mikhaylov.web@biganto.com', 'password': 'nDC0A7Iy1myt'}, params=API_QS)



#### Создание API
Простейший
@mod.route('/qr')
def genirate(tour_id=None):
    print(dir(requests))
    return 'asdads', 202

#### Основные методы reque
