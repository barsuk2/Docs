### redis

#### Команды

redis-cli - запуск клиента

>keys* -вывести все ключи
>FLUSHDB -Очистить текущую базу данных
> HKEYS "jobs:tour-copy.99" -вывести ключи хеша
> HGET "jobs:tour-copy.99" "complite" - вывести значение ключа хеша
> HGETALL - получить все пары ключ значение хеша
> set key value - добавить новую пару 
> set 'egro' 'qweqw'
> get 'egro' - получить значение ключа

#### время жизни объекта.
redis 127.0.0.1:6379> ttl test:1:string - посмотреть время жизни. если -1, то ю=бесконечно
(integer) -1
redis 127.0.0.1:6379> expire test:1:string 6000 - установимть нововый интервал
(integer) 1
redis 127.0.0.1:6379> ttl test:1:string
(integer) 5997


###  классы работающие с REDIS

#### BgJobState

https://docs.google.com/document/d/1_0CoJs8jH8PtReuyMCJ2Vi-qSXkWWrp6bnl2bTl7kUU/edit

Этот класс нужен для записи в РЕДИС этапов работы. 







