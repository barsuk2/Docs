## Java scrypt
### Объвление пременых
#### Устаревший способ объвление переменных hoisting или "всплытие переменных". Переменная может быть выведена в консоль до ее объявления
var a;
var скорее всего глобальная переменная

#### Встроенные функции
setTimeout(functon, 5000); - запуск функции через таймер
alert('HELLO') - всплывающее окно\
typeof var - тип переменной



#### Современный способ объявления переменных
let a;
let s = 3;
const d = 10;

### jsdoc - стандарт документирование кода https://jsdoc.app/tags-param.html
/**
 * @param {string} somebody
 */

ctrl q выводит описание функции

### Режим современного кода

#### "use strict"
##### обявдение переменных без let
>a = 10;
>>ReferenceError: a is not define



### Видимость
#### Обявление переменных без let const var вне строго режима создает переменные в глобальной области видимости window. К ним можно обращатбся как к атрибуту "window"
>a = 10;
>console.log(window.a)
>function f() {a = 10;}
>console.log(window.a)

#### Обявление переменных c var создает переменные в глобальной области видимости window. Объявление внутри функции НЕ СОЗДАЕТ переменную в window. Это справеливо как для строго режима, так и для нестрого.
>var a = 10;
>console(window.a)
>>10

>function f() {var a = 10;}
>console.log(window.a)
>>undefined
#### Обявление переменных c let создает переменные в  области видимости скрипта (script).
#### Обявление переменных c let в блоке (if) создает переменные в  области видимости блока (blocks).
#### Обявление переменных c let в функциисоздает переменные в  области видимости функции (local).

### Где не ставиться точка с запятятой
>if (true) {}

>for (){}

>function(){}
### Где СТАВИТЬСЯ точка с запятятой
#### Если инструкции написаный в одну строку
>let a = 10; let b = 10;
#### В бесконечном цикле
>for (;;);



### Сравение null и undefined
#### Нестрогое стравнеие дает true
#### Строгое стравнеие дает false



### Типы данных
#### Простые (Числа, строки, Логические, null, undefined, Symbol, Bigint )
#### Объекты - Спец. объекты(Массивы, Функции, Дата, Регулярки, Ошибки)



### Привидение типов
#### В строку
>String (2)
>>"2"
#### В число
>Number("2")
>>2

>+"2"
>>2

#### В булево
>>Boolean("")
>false
>>Boolean("1")
>true




### Простое общение с пользователем
#### confirm - простое окно с вопросом и кнопками ДА НЕТ. результат true или false
>const result = confirm("Пользователь на сайте?")
>> true
#### prompt - вопрос с полем ввода. Результат значение поля ввода всегда текст.
>const answer = prompt("вам есть 18 лет", "18" -- значение поумолчанию)
>>18




### Устаревший вывод непосредственно на страницу
>document.write(answers)



### Интерполяция
>const name = "ivan"
>alert(`Привет ${name}`)
>> "Привет Иван"



#### Унарный плюс и минус изменяте тип строки на num
>+"4" + 4
>>8
>-"4" + 10
>>6



### Орператоры
#### ! -отрицание
> 10 == 10
>>true
> 10 == !10
>>false



### Опрераторы сравнения < > >=, <=, ==, === - точное сравние, !== - неравно, %% -and, || - или
>10 =="10";
>>true
>10 === '10';
>>false




## lesson_2
### Условный оператор
#### Синтаксис
>if (условие 1){
>   alert()
>}else if (условие 3){
    alert()
>}else if (условие 3){
    alert()
>}else {
>Прочее}
>



### Оператор switch
#### Синтаксис
>switch (now) {
        case "morning":
            alert("Доброй утро");
            break
        case "night":
            alert("Доброе ночи");
            break
        case "evening":
            alert("Добрый вечер");
            break
        default:
            alert("Добрый день");
    }



### Тернарный оператор
(Условие) ? (Оператор по истине) : (Оператор по лжи);

>let a = 10;
let b = 32;
let my_max = (b>a) ? b : a
alert(` Максимальное число = ${my_max}`)



### Функции
#### Синтаксис function declaration

function имя_функции(параметр1, параметр2, ...){
   Действия
   return
}

>function compare_num(x, y) {
        if (x >= y)
            alert(`Max = ${x}`);
        else
            alert(`Max = ${y}`);

    }
> compare_num () - выполнеие функции



### Анонимная функция
#### Синтаксис function expression -

const name = function (arg){body};
>name (arg) - в переменной содержится результат выполния функции

>const ExprFunc = function (name) {
    return `hello ${name}`
}

>console.log(ExprFunc('egor'))

### Стрелочная функция - анонимная функция
const имя_функции = () => тело функции
const calc = a=> a**2
const calc = (a,b)=> a+b

>const ArrayFunc =  () => `здравствуй дорогой ${name}`
>console.log(ArrayFunc('egor'))

или
const имя_функции = () => {тело функции
    return result};
#### если в стелочной функции используется {}
то нужно вставить return





### Инкремент(увеличение)  декремент(уменьшение) постфикс префикс
#### Синтаксис
a++   - увелисение числа на единицу
#### Префиксная форма
#### Переменной result присваивается значение а с инкрементом
>let a = 10;
const result = ++a;
console.log(`a = ${a}`)
console.log(`result = ${result}`)
>>a = 11
>>result = 11

#### Постфиксная форма
##### переменной result вначале присваивается значение а, потом идет инкремент a
>let a = 10;
const result = a++;
console.log(`a = ${a}`)
console.log(`result = ${result}`)
>>a = 11
>>result = 10




### Инкремент(увеличение)  декремент(уменьшение) постфикс префикс
#### Синтаксис
a++   - увелисение числа на единицу
#### Префиксная форма
#### Переменной result присваивается значение а с инкрементом
>let a = 10;
const result = ++a;
console.log(`a = ${a}`)
console.log(`result = ${result}`)
>>a = 11
>>result = 11

#### Постфиксная форма
##### переменной result вначале присваивается значение а, потом идет инкремент a
>let a = 10;
const result = a++;
console.log(`a = ${a}`)
console.log(`result = ${result}`)
>>a = 11
>>result = 10






### Циклы

#### ForEach()
Метод «arr.forEach(callback[, thisArg])» используется для перебора массива.
Он для каждого элемента массива вызывает функцию callback.
    var arr = ["Яблоко", "Апельсин", "Груша"];
    arr.forEach(function (item, i, arr){
        alert(i + ':'+ item + ':'+ arr)
#### while (условие) { тело цикла}
#### for (let i=0; ind<10; ind++ )
#### for (;;) - бесконечный цикл
#### break - преравть цикл
#### continue - прекратить исполние цикла и перейтий началу цикла. смыс - пропустить однцу итерацию



### Массив
#### let s =[] - пустой,
s[0] - нулевой объект массива
s[0][0] - нулевой объект двумерного массива

s[0].name - общение к вложенному объекту
s[0]['name']

s[1]=1; добавить по индексу



### Оператор спред spread ...
arr1 = [1,2,3]
arr2 = [1,2,..arr1, 3] - добавить существующий массив в другой
#### Копирование  массива
arr3 = [...arr1]
#### Преобразование строки в массив элементов
arr3 = [..."12345"]
>> [1,2,3,4,5]



#### Реструктуризация массива
[a,b,c,d,e] = arr3
[a,,,,e] = arr3 - получаем первый и последный элемент
obj = {}
[obj.id,obj.name]= "1 egor"

[a,b,n,....other] = "1,2,3,4,5,6,6,7,87,"
значение по умолчанию
[drink = "coffee", dessert = "donut"]=['tea']
>>drink = tea



#### Реструктуризация объекта
const user = {id:3,name:"sd', role: 'asdasd', url: 'http://asdads.ru'}
{id,name,role} = user -имена переменных должны совпадать со свойисывми объекта
или
{id:nomer,name: imya, role: rol} = user
{id} = nomer - только один



### Объекты (словарь, хеш-таблица)
#### let a = {} - путой объект, a.name = 'egor' - задать свойств,
#### получить значение
a.name
a['name']
a.images.[] - если вложенный массив
a.url.vk - если вложенный словарь (объект)


#### Инициилизация объекта
#### let s = {name:"sdf",birth: "10.10.2012"};



### Обход массива в цикле
>let s = [1, 2, 3, 4, 5];
>let w = {name :'egio', age : 23}
>for (let i = 0; i <= s.length; i++){
    console.log(String(i)+" = "+i)}
>
>for (let i of s){
>  console.log(i) - обход значений
>
>}
>
### Обход словаря (объекта) в цикле
>for (let i in w){
>   console.log(i) - получим ключи
>   console.log(w[i]) - получим значение
>};

#### Проверка на вхождение
>console.log(1 in s)
>>true
>console.log("name" in w)
>>true



### длина массива, сторки
>s.lingth
>"qwe".length



### Методы массивов
>array.forEach(function) - применят функцию к массиву (map() в python)
>array.pop() - возврат последнего
>array.push(elrm1,elem2,....) - добавление элеменота-ов в конец'
>array.shift() - возврат первого
>array.unshift() - добавить первый
>array.filter() - добавить первый

#%%

l = ["васил","фывфыв","cvb","васил"]
print([s for s in filter(lambda x: x[0] == 'в', l)])



### Объектно-ориентрованное программирование ООП OOP
#### ООП в JS реализовано на уровне объектов
#### Создание конструктора объектов
const Obj(arg,arg2){
    this.arg = arg
    this.arg2 = arg2
    }
#### создание экземпляра
obj1 = new Obj("arg",'"arg2")
obj2 = new Obj("arg",'"arg2")
#### Методы могут создаваться внутри конструктора, но это не практикуется из-за не экономного расходывания памяти.
Методы создаются на уровне прототипа объекта.
Obj.prototype = objprorto
const objprorto = {
    show():{
    return "some result"}
}





#### Или, согласно новому ситнаксису
>Obj.prototype.show = function () {"body function"}



### Стандарт es6
#### Наследоваине атрибутов (свойств)

function AttachedPost(author, text) {
    Post_es5.call(this, author, text)
    this.highlighted = false}

#### Наследоваине методов
AttachedPost.prototype = Object.create(Post_es5.prototype);
AttachedPost.prototype.constructor = AttachedPost;




### Стандарт es6
#### Class - классы
#### Синтаксис
class My_class {
    constructor (arg1,arg2){
    this.arg1 = arg1
    this.arg2 = arg2
    }
    my_method {}
}

### Наследоваине
class My_class extends Parent_class{
    constructor (arg1,arg2,arg3){
    supper(arg1,arg2);
    }
    my_method {}
}



### DOM (documents object model) объктная модель документа - это программный API для HTML XML. DOM предоставляет структированинное представление документа и определяет то, как эта структура может быть доступна из программ, которые могут изменять содеожимое менять стиль и т д. DOM - это API браузера для доступа к HTML.



#### объект window-help
Объект window представляет собой окно, содержащее DOM документ;
В браузерах, поддерживающих вкладки, таком как Firefox, каждая вкладка содержит свой собственный объект window (и если вы пишете расширение, окно браузера тоже является отдельным объектом window
#### Объекты window
innerHeight - возвращает высоту видимой области окна
load - наступает, когда загрузилась вся страница, включая стили, картинки и другие ресурсы.
onload="скрипт"  - Событие onload используется как указатель, что веб-страница полностью загружена,
window.addEventListener("load", function () {
        alert("все картинки загружены")
    });



#### объект document   -help - центальный объект для доступа к странице
document - структура выб докумнета <head><body> ...
>console.dir(document) - стрница как объект
>console.dir(document) - стрница как объект
или
console.dir(window.document) - стрница как объект
#### Объекты document
document.body.offsetHeight - возвращает высоту документа, тега body



### Система координат
offsettop - от левого угла до левого верхнего угла объект
offsetleft
clientWidth - высота ширина блок с padding без margin
clientHeight
scrollHeight - высота всего блока с прокруткой

(box.scrollTop) - высота промотоки блока box от верхнего угла

getBoundingClientRect - получение всех текущих координат
getComputedStyle(box) - получение стилей из css для box. необходим для доступа к псевдостилям
const style_box = window.getComputedStyle(btn, 'hover').backgroundColor
document.documentElement.clientWidth - ширина окна браузер
document.documentElement.scrollTop -промотка документа
document.documentElement.scrollTop = 0 - изменить scrollTop
window.scrollBy (x,y) - перейти на позицию x y относительно текущей позиции
window.scrollTo (x,y) - перейти на позицию x y относительно абсолютных координат
pageYOffset - свойство окна Window , доступное только для чтения. Это то же свойство, что и scrollY и, как таковое, оно тоже возвращает количество пикселей, на которое прокручен документ по вертикали



### Выборки
#### выборка по id
let one = document.getElementById("circle")


>documents.querySelection('p').id = "new_id" - назначить новый ID
#### выборка по тегу
let two = document.getElementsByTagName("a")
>>HTMLCollection - возвращается HTMLCollection
#### выборка по классу
let three = document.getElementsByClassName("class_circle")
>>HTMLCollection - возвращается HTMLCollection
#### выборка по css селектору

let four = document.querySelectorAll('.qwe form[name ="qwe"]')
>>NodeList - возвращается NodeList

let four = document.querySelector('.qwe form[name ="qwe"]')
>>NodeList - возвращается NodeList



#### выборка по name
const six = document.getElementsByName('user')
>>NodeList - возвращается NodeList



#### альтернативные выборки
documents.images - картинки
documents.links - картинки
.menu - это класс 
>#id это id 
document.querySelector('.menu').children - все теги внутри
document.querySelector('.menu').querySelector('span') -  тег внутри класса
document.querySelector('span').parentNode - получить родителя относитьельно тега span
document.querySelector('.prod').childNodes - получить все child nods



### РАбота с текстом
document.querySelector('.div_1').innerText - только видимый текст
document.querySelector('.div_1').textContent - выводит весть текст
document.querySelector('.div_1').textContent.trim() - удалить краевые пробельне символы



### Добавть элемент на страниу
#### createElement
let paragraph = document.createElement('p') - создание элемента
document.body.appendChild(paragraph) - вставляем перед закрывающися тегом
paragraph.innerText = "hello world" - устанавливаем зничение свойству innerText

document.querySelector(".close").getAttribute('data-dismiss') - получить атрибут

#### insertBefore

let hello = documents.createTextNode("hello world") - создадим тестовый узел
documents.body.insertBefore(hello,documents.querySelector("button")) - вставить элемент после button

#### Встсавка элеменов - дополнительный insertAdjacentHTML
beforebegin - перед открывающим тегом
afterbegin - после открытого тега
beforeend  - до закрфтого тега
afterend - после закрытого тега
document.querySelector('body').insertAdjacentHTML("afterbegin","<h1>  hello world  </h1>")



### удаление элемента (узла)

documents.querySelector("button").remove()


### замена элемента (узла)
    let p = document.querySelector('p');
    let h2 = document.createElement('h2');
    h2.innerText = "hello world";
            //newChild, oldChild
    p.parentNode.replaceChild(h2, p);



### Работа с классами
const paragraph  = document.querySelector('p') - работа с классами
paragraph.classList.add - Добавить класс
paragraph.classList.contains - проверить на наличие класса
paragraph.classList.remove - удалить класс
paragraph.classList.toggle - удалить класс если сеществует или создать клас, если не существует



### Вставка HTML
>let qwe = document.querySelector(".menu")
>qwe.innerHTML = "<a href=\"#\">link</a>" - заменяем значение атрибута innerHTML на новое



### Управление атрибутами
document.querySelector("h1").setAttribute('data-one','один') - установать атрибут
document.querySelector("h1").setAttribute('id','new_id') - установать атрибут
console.log(document.querySelector("h1"))

😈️

## Обработчик событий  [event-help]
### События addEventListener - добавить слушителя событий
#### Синтаксис
document.add EventListener("событие", 'функция')
#### события
load - функция выполниться, когдв все загрузиться
document.addEventListener('DOMContentLoaded', function()) - ожидает загрузеи всех тегов HTML (другой контент может продолать загружаться)
'click' - клик
"mouseover" - наводим
keydown - нажатие клавиши event.code = "Escape" -  в интернете
change - возникает когда уходит из фокуса
input - меняется значение
event.preventDefault(); -отключить стандартное реагирование браузера



#### Функция обр события внешняя
    let btn = document.querySelectorAll('.close');

let closeClickHandler = function (event) {
        event.currentTarget.parentNode.style = "display: none;"
    }

    btn.forEach(function (arg) {
        arg.addEventListener('click', closeClickHandler)

    })
    sdfsdf.style.display = "none"



### События addEventListener - добавить слушителя событий
#### Синтаксис
document.addEventListener("событие", 'функция')
#### события
load - функция выполниться, когдв все загрузиться
document.addEventListener('DOMContentLoaded', function()) - ожидает загрузеи всех тегов HTML (другой контент может продолать загружаться)
'click' - клик
"mouseover" - наводим
#### Удалить обраьотчик события
removeEventListener



### Работа с датой data time
now = new Date(); - создается экземпляр объекта Date
const now = new Date('2020-12-21'); - преобразовать строку в дату
const now1 = new Date(1976,0,19, 20); - через список время выводиться с учетом часового
const now1 = new Date(1976,3,19, 20,16,13); время выводиться с учетом часового пояса
const now3 = new Date(0); в милисекундах
1970-01-01T00:00:00.000Z
const now3 = new Date(-898989898998); в милисекундах
1941-07-07T00:35:01.002Z
s = Date.parse



#### Методы data
now.getFullYear(
console.log(now.getMonth()); - год
console.log(now.getDate()) - день
console.log(now.getDay()); - день недели
console.log(now.getUTCHours()); - вемя по гринвичу
console.log(now.getTimezoneOffset()); - разница в минутах от гринвича
console.log(now.getTime()); - поолучить unix date

console.log(now.setHours(18)); - уствноваит новое время



#### выполнение скрипта через интревал
const timer = setTimeout (function,1000) - единоразое выполние функции через 1000 ms
const timer = setTimeout(() =>{alert('hello')}, 6000)
clearInterval(timer) - остановка таймера. РАботет для обеих функций
рекурсивный setTimeout

let id = setTimeout(function log() {
    console.log('hello')
    id = setTimeout(log,500)
},500)
clearInterval(id)

#### CSS selectorr
https://learn.javascript.ru/css-selectors

* – любые элементы.
div – элементы с таким тегом.
#id – элемент с данным id.
.class – элементы с таким классом.
[name="value"] – селекторы на атрибут (см. далее).
:visited – «псевдоклассы», остальные разные условия на элемент (см. далее).
.c1.c2 – элементы одновременно с двумя классами c1 и c2
a#id.c1.c2:visited – элемент a с данным id, классами c1 и c2, и псевдоклассом visited

#### Создание модального окна



### data-attribute - произвольный элемент тега начинающийся на data: пример
<button data-modal>push me




#### альтернативные выборки
documents.images - картинки
documents.links - картинки

document.querySelector('.menu').children - все теги внутри
document.querySelector('.menu').querySelector('span') -  тег внутри класса
document.querySelector('span').parentNode - получить родителя относитьельно span
document.querySelector('.prod').childNodes - получить все child nods



### РАбота с текстом
document.querySelector('.div_1').innerText - только видимый текст
document.querySelector('.div_1').textContent - выводит весть текст
document.querySelector('.div_1').textContent.trim() - удалить краевые пробельне символы



### Добавть элемент на страниу
#### createElement
let paragraph = document.createElement('p') - создание элемента
document.body.appendChild(paragraph) - вставляем перед закрывающися тегом
paragraph.innerText = "hello world" - устанавливаем зничение свойству innerText

document.querySelector(".close").getAttribute('data-dismiss') - получить атрибут

#### insertBefore

let hello = documents.createTextNode("hello world") - создадим тестовый узел
documents.body.insertBefore(hello,documents.querySelector("button")) - вставить элемент после button

#### Встсавка элеменов - дополнительный insertAdjacentHTML
beforebegin - перед открывающим тегом
afterbegin - после открытого тега
beforeend  - до закрфтого тега
afterend - после закрытого тега
document.querySelector('body').insertAdjacentHTML("afterbegin","<h1>  hello world  </h1>")



### удаление элемента (узла)

documents.querySelector("button").remove()


### замена элемента (узла)
    let p = document.querySelector('p');
    let h2 = document.createElement('h2');
    h2.innerText = "hello world";
            //newChild, oldChild
    p.parentNode.replaceChild(h2, p);



### Работа с классами
const paragraph  = document.querySelector('p') - работа с классами
paragraph.classList.add - Добавить класс
paragraph.classList.remove - удалить класс
paragraph.classList.toggle - удалить класс если сеществует или создать клас, если не существует



### Вставка HTML
>let qwe = document.querySelector(".menu")
>qwe.innerHTML = "<a href=\"#\">link</a>" - заменяем значение атрибута innerHTML на новое



### Управление атрибутами
document.querySelector("h1").setAttribute('data-one','один') - установать атрибут
document.querySelector("h1").setAttribute('id','new_id') - установать атрибут
console.log(document.querySelector("h1"))



### События addEventListener - добавить слушителя событий
#### Синтаксис
document.add EventListener("событие", 'функция')
#### события
load - функция выполниться, когдв все загрузиться
document.addEventListener('DOMContentLoaded', function()) - ожидает загрузеи всех тегов HTML (другой контент может продолать загружаться)
'click' - клик
"mouseover" - наводим
#### Удалитьобраьотчик события



### Работа со стронними библиотеками
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css" integrity="sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay" crossorigin="anonymous">
иконки font awesome фонт
    <script src="https://use.fontawesome.com/53a8054f69.js"></script>

web developer ruler - рулетка
swiperjs.com - навороченный слайдер
https://sweetalert2.github.io - модальный окна
https://mmenujs.com - меню
https://animate.style/ - анимация
<img src="https://picsum.photos/200/200?random=${num}"> - генерация изображений
https://webref.ru/css/value/translatey



### Получение атрибутов
console.log(event.target.dataset)



### CSS-help
### Позиционирование position
 position: absolute - Указывает, что элемент абсолютно позиционирован, при этом другие элементы отображаются на веб-странице словно абсолютно позиционированного элемента и нет.
document.body.style.overflow = "hidden" - запрет проскроливания страницы
document.body.style.overflow = "" - восстановить проскроливания страницы



### CSS3-переходы
https://html5book.ru/css3-transition/
transition - исползуется  для анимации d секундах



### JS-pro
#### JSON-help
JSON.stringify(person) -create json
JSON.parse(ex_json) - разбор json
есть онлайн конверторы json - xml
глубокое копировпание можно сделать с помощью JSON
let clone = JSON.parse(JSON.stringify(person))







MAMP  openserver



AJEX - Asynchronous javascript and XML



### JQUERY - это обертуа над JS ПИШИ МЕНЬШЕ ДЕЛАЙ БОЛЬШЕ
подключается как 
<script type="text/javascript" src="//yastatic.net/jquery/2.1.3/jquery.js"></script>


При использовании для выбора элемента чаще всего используется CSS селекторы.

#### методы

.hide() - скрыть
.dakay() - устрановать паузу
.fadeIn() - постепенно вывести на экран
.text() - вывести весь тектс внутри выборки
.htmд() - вывести  HTML ПЕРВОГО элемента внутри выборки

$trash = $('i.fa.fa-trash') - создаем оьъект JQ  где внутри css селектор. Выбран тег i с двумя классами
#### сцепление
$trash.hide().delay(500).fadeIn(1400)

### Размещение добавление позиционирование
.before() - разместь до
>>$('td.table-secondary a:contains("1536")').before('HELLO ')

.after()
>>$('td.table-secondary a:contains("1536")').after('HELLO')

.append() - разместить после 
>>$(.asd).append('<h1>HELLO</h1>')
$htmk = $('td.table-secondary a').text()
$('.rel_path').append('<h1>'+ $htmk + '</h1>')

.prepend
>>$('td.table-secondary a:contains("1536")').prepend('HELLO 1 ')

#### ОБновление элементов

.replaceWith()
.remove()
.html()
.text()
$('.tsd').text('NEW TEXT')

$ht = $('td.table-secondary a')
$ht.text(function (){
       return 'HELLO' + $(this).text()
   })

  $ht.html(function (){
      return '<h1>' +$(this).text()+'</h1>'


   $ht = $('td.table-secondary a:contains("maps")')
   $ht.html(function (){
       return '<h1>' +$(this).text()+'</h1>'

$('td.table-secondary a:contains("QWSAWQ")').remove()




##### СОБЫТИЯ

    $ht.on('click', function () {
        $(this).removeClass('fa-trash');
        $(this).addClass('fa-trash-o')


##### Обход дерева DOM
.parent() - Прямой родитель текущей выборки
.siblings() Все элементы, находящиеся на одном
уровне с текущей выборкой



