Платежная сиситема stripe
ДЛЯ работы со STRIPE используется библиотека stripe
Ддя подключения к апи срипа используюся токены в конфиге, и при создлании приложения flask app они подтягиваются
STRIPE_PK = 'pk_test_X9pUbwo09Lzg3E7Wo8McmOOl00qVUpFy8c'
STRIPE_SK = 'sk_test_FRlqWymPgEqvItx1RsAPXEUu00o7ydhtxq'
STRIPE_WEBHOOK_SECRET = 'whsec_erqNoFrBMKAMgWzVO9WDbZLJPvA5bun9'
#### Проверем через саЙТ
 регистрируемся
 email confirm
 вход настройки - тарифнвйы план -смнить начстройки
 страйп кастомер ид - пуст
 текущи полан - триал
 заполнил платежнвый адрес триальные кредиь кард стрпна сша
 выщло сообщение тарифный план поменяется
 В настройках активировался МОИ СЧЕТА и "Обновить платежные документы"
#### API stripe
stripe.Custumer - все о покупателе
stripe.Py
stripe.Subscription - все о подписках. Подписка ежемесячно формирует счета

#### PaymentMethod
stripe.PaymentMethod.list(type='card', customer='cus_LdIPBti3uHQOFy') - объект 
__платежые методы__ привязан к субекту customer

stripe.PaymentMethod.attach(p_method.id, customer=customer.id)
stripe.PaymentMethod.detach('pm_1KwQnXJqvqR9owjowEzxgCbr')
stripe.PaymentMethod.retrieve('pm_1KwQqxJqvqR9owjop1XH04R1')
stripe.PaymentMethod.list(type='card', customer='cus_LdhWoBFEKYiAQC')




**получить покупателя по ид**
 s = stripe.Customer.retrieve('cus_LdGB6fdba37KH2')
 
 **есть ли активная подписка**
 s.subscriptions.data id True
 
 **список всех текущих ежемесячных подписок**
 stripe.Subscription.list()

**детали одной текущих ежемесячных подписок**
stripe.Subscription.retrieve('sub_1KvzfUJqv8Dr')

### Создаем stripe Customer
param = {'email': 'super@localhost.ru', 'description': 'super'}
stripe.CUstomer.create(**param)

### Подписка
**Список всех переодических подписок для всех**
_отмененые_
stripe.Subscription.list(status='canceled')

_все_
stripe.Subscription.list()

**удалить немедленно подписку пользователя**
_найти активную подписку_
customer=stripe.Customer.retrieve('cus_LdIPBti3uHQOFy')
customer.subscriptions.data[0].id

_удалить подписку_
stripe.Subscription.delete('sub_1Kw1ovJqvqR9owjoSu3Ym0zj)




