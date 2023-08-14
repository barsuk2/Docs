print(f'\033[2;31;43m {title} \033[0;0m')
print(f"\033[1;31m HELLO \033[0;0m") #красный
print(f"\033[1;32m HELLO \033[0;0m") #green
print(f"\033[1;33m WORLD \033[0;0m") # желтый
print(f"\033[1;37m HELLO \033[0;0m")
print(f"\033[1;35m HELLO \033[0;0m")

### biganto.com-help
#### работа в консоле🤩️
Простые ORM запросы не работают. Нужно создавать контекст приложения

https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
### 
**biganto**
from visual.app import create_app
app= create_app('config.local.py')
app.app_context().push()
from visual.core import db
from visual.models import Tour, Footage, User

del tour.meta['audio']
del tour.footage.meta['skyboxes']['1']['audio']
from sqlalchemy.orm.attributes import flag_modified
flag_modified(tour.footage, 'meta')
flag_modified(tour, 'meta')
db.session.commit()
from sqlalchemy.orm.attributes import flag_modified

**biganto_test**
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
##### Вход в админку после авторизации в ЛС
from roompark.app import create_app
app= create_app('config.local.py')
app.app_context().push()
from roompark.core import db
from roompark.models.estates import Estate
app = create_app('config.test.py')
    with app.app_context():
        db.drop_all()
        db.create_all()

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

#### Использование терминала для тестирования отправки email 

with app.test_request_context():
    send_email(
        gettext('Tour "%(title)s" successfully created', title=(tour.title if tour.title else gettext('Untitled'))),
        [tour.user.email],
        'no-reply@biganto.com',
        template='mail/build_success',
        tour=tour
    )
    

