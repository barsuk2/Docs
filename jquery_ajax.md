### JQUERY - это обертка над JS ПИШИ МЕНЬШЕ ДЕЛАЙ БОЛЬШЕ
подключается как 
<script type="text/javascript" src="//yastatic.net/jquery/2.1.3/jquery.js"></script>


При использовании для выбора элемента чаще всего используется CSS селекторы.
### видимость
Методы jQuery .show(),
.h ide() и .toggle() анимируют
отображение и скрытие
элементов.


#### Поиск элеменов
общий синтаксмс
$('')

$('[attr="name"]') - поиск по произвльному атрибуту
$('.c') - поиск по классу c

hasClass() - проверка вхождения класса


#### поиск по формам

$(':text[name="phone1"]').val() - выводим значение инпута с типом текст и именем phone1

$form.find('input:text[name="phone2"]').val(10)) - поиск в найденой форме текстового инпута с именем phone2


$(':input:submit[name="button1"]').val() - выбрать на странице все input все кнопки с именем
$(':input:[name="button1"]').val() - выбрать на странице все input с именем
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



#### ajax как функция jqurey
https://basicweb.ru/jquery/jquery_method_ajax.php

$.ajax( url, {settings} )

### alax как XMLHttpRequest

var xhr = new XMLHttpRequest();
            xhr.open('POST', '/admin/test_', true)
            xhr.send()
            xhr.onload = function () {
                if (xhr.status === 200)

#### ajax как методы JQUERY
#### $.post

		$.post(url_, $form.serialize(), function (data){
                var res = $.parseJSON(data)
                $result1.html('<a href="">res.lname</a>')
                $result2.html('<h6>res.phone</h6>')



#### $.ajax

		$.ajax({
                type: "POST",
                url: url_,
                data: $form.serialize(),
                success: function (data) {
                    let res = $.parseJSON(data)
                    $result1.html(`<a href=""> press button 2 ${res.lname}</a>`)
                    $result2.text(res.phone)

                }
            })


##### Промисы

https://habr.com/ru/post/439746/

promise = new Promise((resolve, reject) => {if (randomNumber < .7) {
                resolve('Все прошло отлично!');
            } else {
                reject(new Error('Что-то пошло не так'));
            }
        });
        promise.then((data) => {
                console.log(data);  // вывести 'Все прошло отлично!'
            },
            (error) => {
                console.log(error); // вывести ошибку})

#### fetch

fet

