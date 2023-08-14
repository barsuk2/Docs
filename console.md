print(f"\033[m\033[30m {} \033[0m")  # красный
print(f"\033[0m\033[32m ** \033[31m {} \033[32m ** \033[0m")  # крассный
print(f"\033[m\033[31m {} \033[0m")  # зеленый
print(f"\033[m\033[32m {} \033[0m")  # 
print(f"\033[m\033[33m {} \033[0m")  # желтый
print(f"\033[m\033[34m {} \033[0m")  # фиолдет
print(f"\033[m\033[35m {} \033[0m")  # голуб
print(f"\033[m\033[36m {} \033[0m")  # зеленый
print(f"\033[m\033[37m {} \033[0m")  # белый
### biganto.com-help
#### работа в консоле🤩️
Простые ORM запросы не работают. Нужно создавать контекст приложения

https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
### biganto
from visual.app import create_app
app = create_app('config.local.py')
app.app_context().push()
from visual.core import db
from visual.models import Tour, Footage, User
from visual.models import BROffice, BROperator, BROrder, BROrderAsset

### task_tracker
from app import create_app
app = create_app()
app.app_context().push()
from core import db

with app.app_context():
    db.create_all()


### biganto_test
from visual.app import create_app
app= create_app('config.test.py')
app.app_context().push()
from visual.core import db
from visual.models import Tour, Footage, User


### bogenhouse
from bogenhouse.app import create_app
app= create_app('config.local.py')
app.app_context().push()
from bogenhouse.core import db
from bogenhouse.models.estates import Estate
Estate.query.all()


### room-park
from roompark.app import create_app
app= create_app('config.local.py')
app.app_context().push()
from roompark.core import db
from roompark.models.estates import Estate

Estate.query.all()
from bogenhouse.models.documents import Document
from bogenhouse import create_app

app = create_app('config.local.py')

with app.app_context():
    Document.query.all()


##### РАбота с API

### http запросы


#### Простой GET 
### готовый запрос, выводит список туров пользователя
import requests
B_URL='http://local.biganto.com'
API_QS = {'client': 'web', 'client_version': '1.0'}
rv = requests.get(f'{B_URL}/api/v3/tours', params=API_QS)
API_TOURS =API_QS.copy()
API_TOURS['user_id']=3
rv = requests.get(f'{B_URL}/api/v3/tours', params=API_TOURS)

#### если STATUS 200
>rv.json() 

rv = requests.get(f'{B_URL}/api/v3/tours', params={'client': 'web', 'client_version': '1.0','user_id': '9'})

tours_rv = sess.get(f'{B_URL}/api/v3/tours', params={'client': 'web', 'client_version': '1.0','user_id':9})

### AUTH 🇦🇪️
import requests
B_URL='http://local.biganto.com'
API_QS = {'client': 'web', 'client_version': '1.0'}
API_TOURS =API_QS.copy()
user = requests.post(f'{B_URL}/api/v3/users/login', json={'email': 'kasiatora@localhost.ru', 'password': '123'}, params=API_QS)
API_TOURS['auth_token'] = user.json()['result'].get('token')
rv = requests.get(f'{B_URL}/api/v3/tours/3/qr', params=API_TOURS)

API_TOURS['auth_token'] = '9|CZS_gtlqbWaezh0zuDpJ-5uCwYvTUy9fEUYBsUXKfUeXL00ERU7Dj81Zb3I6zIlwEOg7BRaQNjT7HZlj-TB8-A=='

B_URL='https://biganto.com'
user = requests.post(f'{B_URL}/api/v3/users/login', json={'email': 'mikhaylov.web@biganto.com', 'password': 'nDC0A7Iy1myt'}, params=API_QS)

Ghaidaa Kadhim Kareem AL-Saadi
TR09 0001 0025 8180 6399 6050 03
#### Использование терминала для тестирования отправки email 

with app.test_request_context():
    send_email(
        gettext('Tour "%(title)s" successfully created', title=(tour.title if tour.title else gettext('Untitled'))),
        [tour.user.email],
        'no-reply@biganto.com',
        template='mail/build_success',
        tour=tour
    )
    

