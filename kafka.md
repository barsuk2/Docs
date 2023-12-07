./kafka-topics.sh --list --zookeeper zookeeper:2181 - список топиков

### Kafka CLI
### wurstmeister/kafka - образ докера в проекте
* /opt/kafka/bin/ * - путь к Kafka CLI

Источник: https://internet-34.ru/kak-rabotat-s-kafka-cli

./kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic myTopic - Создание топика

./kafka-topics.sh --list --zookeeper zookeeper:2181 - эта команда из под контенера kafka-cli
./kafka-topics.sh --list --bootstrap-server localhost:9092 - эта команда из под контенера kafka

3. Отправка сообщения в топик:

./kafka-console-producer.sh --broker-list kafka:9092 --topic myTopic

4. Чтение сообщений из топика:

./kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic myTopic --from-beginning

5. Отображение оффсетов для группы потребителей:

./kafka-consumer-groups.sh --bootstrap-server kafka:9092 --list

./kafka-consumer-groups.sh --bootstrap-server kafka:9092 --group myGroup --describe



### zookeeper
#### wurstmeister/zookeeper - image
https://programmer.group/zookeeper-command-line-tool-zkcli.sh.html
/opt/zookeeper-3.4.13/conf/zoo.cfg
/opt/zookeeper-3.4.13/bin/ - исполняемыые скрипты
dataDir=/opt/zookeeper-3.4.13/data - 

### kafka
#### wurstmeister/kafka
/opt/kafka/bin - исполняемыые скрипты kafka-cli
Сокращеня
К - Консюмер



Термины
fetch - приносит
send - отпрвляее
ACK/NACK - ПОДТВЕРДИТЬ/ ЗАБЛОКИРОВАТЬ
topic - тема
partitions - парртиция
retention - удержание
Тип данных в кафке это реплицированный log

Тезисы:
Сообщения организованы и хроятся в Topics, какждый топик состоит из 1 или более партиций распределеных между брокерами внутри одного кластера
Когда сообщение поступает в брокер оно записываеся в одну из партиций этого топика
Сообщения с одинаковыми ключами => в одну партицию
кафка гарантирвет очередность в рамка ходной паритиции
Для гарантии каждая партиция может быть реплицированна n раз, (n - replication factor)
У каждой партиции есть один брокер лидер(Leader). В него записываются все сообщения 
У каждго Лилера есть 0,,N последователей(Follower)
Чтобы понять кто является Лидером, клиент делает запрос к мета данным

Каждому записанному сообщению назначается offset - униепльный, монотонно возрастающий 64 битное число.
Данный хранятся согласно заданной конфигурации ретеншена (retention)
retention.ms - минимальное время хранения
retention.bytes - максимальный размер паритиции

### Консюмер
Каждый К чаще всего является сачть кайой нибудь группы. Имеет уникальное название и регистрирутется в кластере Кафки. Даные из одного топика могут прочитаны разными К групп. Каждый член группы читает из разных паритиций топика. Таким образом распределяя нарузку. Паритици назначаются Ком уникально, чтобы избежать повторной обработки. Если К не справляются с объемом данных, ты нужно сделать новую партицию
Механизм пртционирования- это механизми маштабирования
Добавлять паритици можно налету без остановки бркеров. Клиент автоматически узнают о новой паритици из мета данных
### Важно
1. При добавлении новой партиции может сломаться порядок
2. Партиции не возможно удалить после их создания. Можно ужалить весь топик целиком
3. Если добавляется паритици на проде, где пишутся сообщения НЕ ЗАЮЫВАТЬ auto.offset.reset. Данный могут не обработаться из задержки в обновлении метаданныйх 

#### 

Партиции не бесплатны. Каждая кваличивает время старта брокера и выбор лидеров после падения. Теоретический лимит на кластер 200000 партици для кафка 2.0

Можно добавить несколько К групп, который будут читать те же паритции со своей скоростью и логикой

### K offset маханизм


#### zookeeper  
Что такое Apache Zookeeper?

Zookeeper - один из важных компонентов кластера Kafka, который выполняет роль консистентного хранилища метаданных. В настоящее время Zookeeper является критической зависимостью для Kafka, поскольку именно он способен сказать, живы ли брокеры, какой из брокеров является контроллером, а также в каком состоянии находятся лидеры партиций и их реплики. Важно помнить, что падение Zookeeper равнозначно падению всего кластера Kafka! Поэтому эта система также нуждается в поддержке и обновлении. Но, к счастью, нагрузка на Zookeeper при нормальной работе кластера является минимальной.
Падение zookeeper к разрушению кластера

#### Запуск кластера из одной ноды
Если вы работаете на нашем стенде, архив с кафкой мы уже скачали заранее :)

Копируем архив в домашний каталог:

cp /opt/kafka_2.13-2.7.0.tgz ~/
В случае, если что-то пойдет не так, вы сможете удалить каталог с кафкой полностью и взять чистый архив для того, чтобы начать практику с начала. Если вы его случайно удалили, можно скачать архив по ссылке:

wget https://archive.apache.org/dist/kafka/2.7.0/kafka_2.13-2.7.0.tgz
Распакуем архив и перейдем в каталог с приложением:

tar -xzf kafka_2.13-2.7.0.tgz
cd kafka_2.13-2.7.0
Первым делом мы запускаем Zookeeper. Как мы уже обсуждали, Кафка пользуется зукипером для хранения метаданных, а также для координации своей работы (выбора лидеров партиций и контроллера).

./bin/zookeeper-server-start.sh config/zookeeper.properties
Запускаем брокер Кафки

./bin/kafka-server-start.sh config/server.properties

#### Создать топик
Запуск кластера из одной ноды
Если вы работаете на нашем стенде, архив с кафкой мы уже скачали заранее :)

Копируем архив в домашний каталог:

cp /opt/kafka_2.13-2.7.0.tgz ~/
В случае, если что-то пойдет не так, вы сможете удалить каталог с кафкой полностью и взять чистый архив для того, чтобы начать практику с начала. Если вы его случайно удалили, можно скачать архив по ссылке:

wget https://archive.apache.org/dist/kafka/2.7.0/kafka_2.13-2.7.0.tgz
Распакуем архив и перейдем в каталог с приложением:

tar -xzf kafka_2.13-2.7.0.tgz
cd kafka_2.13-2.7.0
Первым делом мы запускаем Zookeeper. Как мы уже обсуждали, Кафка пользуется зукипером для хранения метаданных, а также для координации своей работы (выбора лидеров партиций и контроллера).

./bin/zookeeper-server-start.sh config/zookeeper.properties
Запускаем брокер Кафки
### создание
./kafka-topics.sh --create --topic registrations --bootstrap-server localhost:9092
### информация о топике
./kafka-topics.sh --describe --topic registrations --bootstrap-server localhost:9092
### отрпаить сообщене в топик
./kafka-console-producer.sh --topic registrations --bootstrap-server localhost:9092

#### читать из топика
./kafka-console-consumer.sh --topic registrations --bootstrap-server localhost:9092 --consumer-property auto.offset.reset=earliest

--consumer-property auto.offset.reset=earliest - читать с самог раннего
или так
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic registrations --from-beginning

#### Получиьт сообщения группой
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic registrations --from-beginning --group slurm

#### описание группы
./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group slurm --describe

#### сбросить offset на начало
./bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group slurm --to-earliest --reset-offsets --execute --topic registrations


