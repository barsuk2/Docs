### Очередь, фоговые задачи

Это способ форсмровать выпольнеие задач виде очереди из задач.

#### Модуль RQ 

Данный модуль непосредственно связан с REDIS. 

Для создания обработчика очереди ипользуется 
rq worker

В biganto Воркер запускается вместе с сервером./runserver
rq worker default quick - запускается две очереди 

В core.py создается очередь со строноы приложения
from redis import Redis
from rq import Queue
queue = Queue(default_timeout='12h', connection=Redis)

в едпоинт создается очередь
    job = queue.enqueue('visual.jobs.admin.copy_tour',
                              tour.id, title, copy_footage, copy_meta, folder_id,
                              result_ttl=current_app.config.get('REDIS_EXPIRE_TIME'),
                              description=f'{tour_id}-{title}',
                              job_id=f'copy_tour:{tour_id}-{title}',
                              job_timeout=current_app.config['BUILDER_JOB_TIMEOUT'])


В visual/jobs/admin.py хранятся функции для очередей

