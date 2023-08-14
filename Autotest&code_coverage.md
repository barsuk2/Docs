###
Фикстура

без наличияхотя бы отдного теста фикстуры и начальные данные не отрабатываются


1. Создаем клиента - основной рабочий механзм автотестирования. Происходит запуск сервера фласк в фоновом режиме. 

@pytest.fixture(scope='module')
def client():
    app = create_app(cfg='config.test.py')
    with app.test_client() as client:
        yield client

pytest --cov-report term --cov=visual.api3 вывести в терминал покрытие для api3
pytest --cov-report html:cov_html --cov=visual.api3 создать html отчет


--tb=[auto/long/short/line/native/no]: Управляет стилем трассировки.
-v / --verbose: Отображает все имена тестов, пройденных или не пройденных.
-l / --showlocals: Отображает локальные переменные рядом с трассировкой стека.
-lf / --last-failed: Запускает только тесты, которые завершились неудачей.
-x / --exitfirst: Останавливает тестовую сессию при первом сбое.
--pdb: Запускает интерактивный сеанс отладки в точке сбоя.

scope='function'
scope='module'
scope='session'

pytest tests/test_api_users.py::test_api_auth -vs
