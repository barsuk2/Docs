all() -  Проверяет, что все элементы в последовательности True.
any() - Проверяет, что хотя бы один элемент в последовательности True.

### Фйлы
file-help
file = open('example1.txt','r', encoding='utf-8')
#### методы
file.close()	закрывает открытый файл
file.close()	закрывает открытый файл
file.fileno()	возвращает целочисленный дескриптор файла
file.flush()	очищает внутренний буфер
file.isatty()	возвращает True, если файл привязан к терминалу
file.next()	возвращает следующую строку файла
file.read(n)	чтение первых n символов файла
file.readline()	читает одну строчку строки или файла
file.readlines()	читает и возвращает список всех строк в файле
file.seek(offset[,whene])	устанавливает текущую позицию в файле

#%%

file = open('My-dict_en_ru.txt',encoding="utf-8")
print(file.close())



### исключения
try-help
except-help

try: - попробывать
    10 /0
except Exception as e: тект оштбки в s
    print(e)
finally:
    print ('выполним в любом случае')

Иногда нужно будет разбираться с проблемами с помощью вызова исключения. Обычная инструкция print тут не сработает.
a,b=int(input()),int(input())  # вводим 1 затем 0
if b==0:
    raise ZeroDivisionError

#%%

try:
    10 /0
except Exception as e:
# except FileNotFoundError:  - конкретная ошибка

    print(e)
finally:
    print ('выполним в любом случае')

### Байтовый строки
'abc'.encode() - преобразует в байт
> b'abc'
> chr(97) вернет символ
> ord('a') вернет число

#### комметнарии
### docstring-help
внутри функции """ Enter """



#### встроенные  функции
vars(__object) - возвращает атрибуты класса как словарь
isinstance(series,dict): является ли словарем



### JSON

dump(data,file) - сериализует data d файл
dumps(data) - сериализует data
with open('num_text.json', 'w') as f:
        f.write(json.dumps(num_text))
>>str

load(date,file) - десериализует data из файла
loads(data) - сериализует data
>>str



### ООП oop-help
Инкапсуляция - размещение в одном компоненте атрибутов и методов, котроые с ним работают. ЗАКРЫТ  от измения из вне. ИЗмение и чтение осуществляется через getter и setter.
public - методы открытого интерфейса
protected - скрытые данные, используем одинарное нижнгее подчеркивание "_"
private - жесткое скрытые данные, используем двойное нижнее подчеркивание "__" . Невидят потомки
user._Users__age -можно получить доступ через name mangling (искажение имени)
self._name = name - скрывет name

#### атрибут класса
class Sdf():
    currency = 'rub' - что-то общее для всех экземпляров
####
class Asd (Gasd):
    def __init__ (self,asd,asd):
        super().__init__ (self,asd,nam,asdsad) - расширить атрибуты У потомка



#### Наследование
class Parent()
    def Method1(self)
class Child(Parent) - класс Child наследует ВСЕ атрибуты и методы

class Child1(Parent)
    def Method1(self) - переопрделяем родительский метод

class Child2(Parent)
    def Method1(self)
    print('word')
     super().Method1()
     print ('hello')    - Создаем оболочку wrapper для родительсякого метода

class Child3(Parent)
    def __init__(atr1,atr2 , atr3): - получить родительские атрибуты и добавить свой
        super().__init__(atr1,atr2) - позвать все родительские атрибуты

     print ('hello')    - Создаем оболочку wrapper для родительсякого метода

class Child4(Parent): - случай, когда экземляр класса не требует обязательных атрибутов
    def __init__(self):
        super().__init__()



переопоределение мотодов
duck typing - плавает как  утка ходит как утка-  это утка



## Полезные функции
Функция sum

#%%

d3 = []
d = [2,3,4]
d1= [3,4,5]
d3.append(d)
d3.append(d1)
print(d3)
print('конкатенация', sum(d3, []))



filter
filter-help, map
для фильтрации к последовательности применят функцию

#%%

# отфильтровывает последовательность по функции
d3 = [2, 3, 4, 3, 4, 5]
print(list(filter(lambda x: x > 3 and x < 5, d3)))

t9 = 'роза упала на лапу азора'

### MAP
# применет к  последовательность функцию
d3 = [2, 3, 4, 3, 4, 5]
print(list(map(lambda x: x *5, d3)))


#### TIME модуль

задержка выполнение кода
time-help
sleep-help
time.sleep(1)- задержка в секундах


#%%

import time
for i in range(3):
    print(i)
    time.sleep(1)



время выполнение ячейки

#%%

%%timeit
for _ in range(10**5):
    a= 30**6



divmode

#%%

a,b = divmod(9,4) # возвращает остаток от деления и частное
print(a ,b)



### functools-help
Модуль functools - сборник функций высокого уровня: взаимодействующих с другими функциями или возвращающие другие функции.

#### reduce
функция reduce сводит значениея последовательность к одному
на основе функции

#%%


import functools
a = [23,213,34,4,68,798,49 ]
a = functools.reduce(lambda x, y: x/y, a)
a



itertools-help
Модуль itertools - сборник полезных итераторов.

#%%

'генерация бесконечной арифмет прогрессии'
import itertools as it
import time

for num in it.count(7,3):
    if num<20:
        print(num)
    time.sleep(1)

#%%

' бесконечной генерация значений из последовательности'
import itertools as it
import time

for num in it.repeat(2,10):
    print(num)
    time.sleep(1)

#%%

' бесконечной генерация значений из последовательности'
import itertools as it
import time
for num in it.cycle('qweasdzxc'):
    print(num)



#%%

' бесконечной генерация значений из последовательности'
import itertools as it
import time
for num in it.accumulate(it.count(2,3)):
    print(num)
    time.sleep(1)

#%%

' бесконечной генерация значений из последовательности'
import itertools as it
import time
for num in it.chain(it.count(7,3),it.cycle('qweasdzxc'),it.repeat(2,10)):
    print(num)
    time.sleep(1)

#%%

import itertools as it
colors = ['белый', 'жёлтый', 'синий', 'красный']
for item in it.combinations(colors, 3):
    print(item)



комбинаторика

#%%

import itertools as it
d =[x for x in it.product('QWER','asdf')]
d

#%%

import itertools as it
list(it.starmap(lambda x,y: f'{x}{y}', [(2,5), (3,2), (10,3)]))



Декоратор

#%%

import time
def exempl_decoration(fn):
    def wrapped(a):
        return 'привет' + fn(a)
    return wrapped

def time_count(fn):
    def wrapper(arg):
        start = time.perf_counter()
        fn(arg)
        finish = time.perf_counter() - start
        print(finish)
    return wrapper
@time_count
@exempl_decoration
def str_(a):
    return a
    

print(str_('hello'))



#### Стандартные библиотеки

os - модкль для работы с ОС
os.path - модуль для работы с путями
sqlite
re
random
match
json
itertools
hashlib
datetime
csv
calendar
sys - Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.
uuid - генерация уникального идентификатора RFC 4122

###РАбота с датой и временной зоной 

datetime.datetime.now() - текущая дата и время
a = datetime.date.today() - текущая дата
now.strftime('%d.%m.%Y') - преобразовывает дату в строку
datetime.datetime.strptime('15.07.2021', '%d.%m.%Y') - преобразовывает строку в дату
dateta

n =datetime.datetime.now()

n = n.date() - преобразование в дату
n.month - извлечь месяц
#### Хэш
https://python-scripts.com/md5-sha1
принимает только битовую строку
преобразоваваем в hex

#%%

import uuid, hashlib
uid=uuid.uuid4().hex
print(hashlib.md5(b'hello').hexdigest())
print(hashlib.md5(b'hello').hexdigest())
print(hashlib.sha256(b'hello' + uid.encode()).hexdigest())
print(hashlib.sha256(b'hello' + uid.encode()).hexdigest())



### Модуль Collect
#### Counter выводит словарь где ключ - эдемент последовательность val -кол-во
most_common(10) - выводит десять самых популярных

#%%

from collections import Counter
c = list(Counter(a=4, b=2).elements())
print(c)

OBJ = Counter('abrakadabra')
print(OBJ)  # -> Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})




#### defaultdict(default_factory) - словарь, вазвращающий 0 , если ключа нет в словаре аналог
метод .get('key','0')
defaultdict(int) - вернет 0
defaultdict(str) - вернет ''
defaultdict(list) - вернет []

defaultdict(list) При указании default_factory объект обладает методами default_factory

defaultdict(list)
DEF_DICT[k].append(v)

defaultdict(str)
for k, v in LST:
    DEF_DICT[k]+=f'{str(v)} '


d = defaultdict(int)
    for word in WORDS:
        d[word] += 1



#### OrderedDict - делает словарь индексируемым. НЕ актуально для версий 3



#### deque Эмитация работы с стеков и очередей.

#%%

from collections import deque
import string

simple_lst = list("bcd")
deq_obj = deque(simple_lst)
print(deq_obj)  # -> deque(['b', 'c', 'd'])

# добавим элемент в конец очереди
deq_obj.append('e')
print(deq_obj)  # -> deque(['b', 'c', 'd', 'e'])

# добавим элемент в начало очереди
deq_obj.appendleft('a')
print(deq_obj)  # -> deque(['a', 'b', 'c', 'd', 'e'])

# pop также работает с обоих концов
deq_obj.pop()
deq_obj.popleft()
print(deq_obj)  # -> deque(['b', 'c', 'd'])

# перемещаем два элемента с конца очереди в начало
deq_obj.rotate(2)
print(deq_obj)

# перемещаем два элемента с начала очереди в конец
deq_obj.rotate(-2)
print(deq_obj)

#%%

from collections import deque
import string

a=deque(string.ascii_uppercase)




####
namedtuple - тип данных, ведущи себя как кортеж, каждому элем присваивается имя
RES = namedtuple('Resume'[имя], 'id first_name second_name' [перечисление через пробелы имена полей])

RESUME_PARTS = RES(
    id='1',
    first_name='Ivan',
    second_name='Ivanov'
)


print(RESUME_PARTS)  # -> Resume(id='1', first_name='Ivan', second_name='Ivanov')
print(RESUME_PARTS.id)  # -> 1



#### Работа с динамической памятью
sys.getrefcount - кол-во ссылок на объект









### Эмпирическая оценка алгоритмов на Python

Оценка времени исполнеиня
модуль timeit
Timer

#%%

from timeit import Timer, timeit


def test_concat():
    my_lst = []
    for i in range(1000):
        my_lst = my_lst + [i]


timer = Timer("test_concat()", "from __main__ import test_concat")
print('concat', timer.timeit(number=1000), 'mSec')

#%%

"""Замеряем обычные блоки кода"""
from timeit import timeit

print(timeit("x = 2 + 2", number=1000))
print(timeit("x = sum(range(10))"))

print(timeit("""
for i in range(3):
    y = i + 2
    a = 4
    if a == y:
        1/2
"""))


#%%

import timeit
"Оcновной вид использования timit"
def concat_test():
    my_lst = []
    for i in range(1000):
        my_lst += [i]

print(timeit.timeit("concat_test()", setup="from __main__ import concat_test", number=1000))

# еще через строку кода
STR_CODE_2 = '''
j = sum(range(1, 1000))
'''
print(timeit.timeit(STR_CODE_2, number=1000))



Профилировка профайлер
Профилирование — сбор характеристик работы программы с целью их дальнейшей оптимизации.



import cProfile
либо timeit либо профайл

def main():
    список функций для проверки


cProfile.run('main()')

#%%

import cProfile
def rande_():
    list(range(100000))

def cycle_():
    l=[]
    for i in range(100000):
        l+=[i]

def main():
    rande_()
    cycle_()

cProfile.run('main()')



### Профилировка затрат памяти
### memories
from memory_profiler import profile
from pympler import asizeof
from copy import deepcopy
@profile
def function_1():
    """Выделяет доп память, не освобождается"""
    x = list(range(100000))
    y = deepcopy(x)
    return y

function_1()


from copy import deepcopy
l=list(range(10))
m=deepcopy(l)
print(id(l), id(m))
del l
print(id(m))



Свой декоратор

import memory_profiler
import time
t1 = time.process_time() - отсечки времени
m1 = memory_profiler.memory_usage() - отсечки памяти - список

m1[0]-m2[0]




Можно использовать модуль numpy для работы с большими объемами





Затраты памяти в разрезе типов данных. Утилита
from guppy import hpy

h = hpy()
... код
print(h.heap())


k.startswith(str) - Метод startswith() проверяет, начинается ли строка с str, необязательно ограничивая согласование с заданными индексами начала и конца.

str.startswith(str, beg = 0,end = len(string));


### colors
ЦВЕТНОЙ ВЫВОД 🎻️
https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html

print(f'\033[2;31;43m {title} \033[0;0m')

### uuid модуль
Генерация уникального в пространстве и времени идентификатора
uuid.uuid4()


#### Сортировки множеств

#### Отсорировать по первому значению (возрастанние)
l1 = [(1,4),(3,5),(2,6)]
sorted(a, key = lambda x : x[0])

#### (убывание)
sorted(a, key = lambda x : x[0], reverse=True)

#### Спсиок словарей
a = [{'name': 'bsd','size': '10'},{'name': 'asd','size': '01'},{'name': 'aad','size': '12'}]

sorted(a, key=lambda x: x['name'])

### сортирвка внутри словаря

a = {'a':[4,5,12,7], 'b': 'fdsdas'}
a['b'] = ''.join(sorted(a['b']))
a['a'] = sorted(a['a'])


