### Важные команды
git diff --stat master..feature/admin-br-assets-edit-delete

## Базовае операции GIT в терминале BUSH

#%%  Использование отдельных различных SSH ключей для различных GIT репозиториев
https://shumiloff.ru/ispolzovanie-otdelnyx-razlichnyx-ssh-klyuchej-dlya-razlichnyx-git-repozitoriev.html
git config --local core.sshCommand 'ssh -i /home/egor/.ssh/barsuk-git'


### Базовае настройки Git
#### git config --global user.name "[name]"  - указывается логин ,который будет записывать за каждым измением
#### git config --global user.mail "[email-address]" - указание E-mail для связи с хозяином изменений
#### git config --global.core.editor "[program]" - указание текстового редактора по умолчанию
### Пример
>C:\Users\egor\GeekBrains\data_analitics>git config --global user.name
mikhailov_egor
>C:\Users\egor\GeekBrains\data_analitics>git config --global user.name "mikhailov_egor"

>C:\Users\egor\GeekBrains\data_analitics>git config --global user.email

>info@geekbrains.com
>C:\Users\egor\GeekBrains\data_analitics>git config --global user.email "ickzn@ya.ru"
>C:\Users\egor\GeekBrains\data_analitics>git config --list -все настройки

#%% md

### Создание нового репозитория как клон удленного
На сайте github.com создаем новый репозитрий. После этого выхcaодит инстукция
echo "# data_analitics" >> README.md
git clone it@github.com:barsuk2/data_analitics.git project - указание папки на лок компьютере

### Создание нового репозитория из локального
Создаем в github репозиторий second-site и и выполняем команды
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:barsuk2/second-site.git
git push -u origin master


### конфигурация github
#### определить origin
> git remote add origin git@github.com:username/repository.git

### посмотреть origin 
> git remote -v

#### переопределить origin
>git remote set-url origin git@github.com:username/repository.git

#%% md

### Клонирование репозитория
git clone it@github.com:barsuk2/data_analitics.git project - указание папки на лок компьютере

#%% md

### управление историей (коммитами)🐷️
##### Отображает измение с коммитами
>git log
##### Отображает измение с коммитами по всем веткам
>git log --all
>git log -2 # Двух последних
>git log --oneline # вывод в упращенном виде
 git log --no-merges master.. - посмотреть не вмерженный commit в master

##### Отображает все измениея в репозитории
>git reflog

##### Восстановить истории коммитов до указанного
>git reset b84aea5

##### Удаляет изменения внесенные коммитом в  репозиторий. Создает новый коммит
>git revert b84aea5

##### Восстанавливает файл до предыдущего коммита
>git revert b84aea5
git restore b84aea5.txt

#%% md



#### временая смена HEAD
git checkout HEAD~1
##### Возврат 
git switch -c new_branch Создать ветку из этого места
git switch - вернуть как было


#### Работа с ветками
##### Посмотреть список веток
>git branch

##### создать ветку
>git branch dev
##### создать ветку и перейти на нее
>git checkout -b feature

##### Создание новой ветки от мастер
>git branch dev-master master


##### Создание копии ветки из удаленного репо
>git checkout branchname

Работает, когда:

Есть удалённая ветка origin/branchname
Но нет локальной ветки с именем branchname


##### Удаление ненужных ветки
>git branch -d dev-master
##### Удаление ненужных ветки на удаленном репо
>git push --delete origin dev-master - одной\
>git push --delete origin dev-master1 dev-master1 - нескольких

#%% md

### Rebase измение места старта ветки
[no_master_branch]>git rebase master
git push --firse

#%% md

#### Версионирование
##### Установим последнему коммиту тег 1.0.0
>git tag 1.0.0
##### Посмотрим список тегов
>git tag --list

##### Загрузить теги на remote repository
>git push --tags
##### Удалить тег (для переноса на новое место)
git tag -d [-- delete]master_version

##### Удалить тег в remove repo(для переноса на новое место)
>git tag -d 1.0.1
>git push --delete origin 1.0.

### Переименовать коммит
git commit --amend
 
#%% md

Сложные операции
1. Переключить ветку имея несохраненные измение [STASH]
2. склеивание коммитов или объединеи всех коммитов в один [SQUASH]
3. Перенос отдельныйх коммитов [Chery Pick]

git stash drop удалить один файл тайнка


#%% md

Переключить ветку имея несохраненные измение [STASH]
### Основные проблемы при работе с Git
##### Переключение веток при несохраненных данных
### Git STASH локальное пространство записывает все текущие измения
#### Перенесем несохраненные изменение в stash
>git stash
#### Просмотр пространства stash
>git stash list
#### После возврата на свою ветку вызываем из stash измения
>git stash pop stash@{1}
#### Дальше продолжаем вносить измениея или коммитим
>git stash push <file>
#### Можно добавить еще файлы в существующий stash

#%% md

2. склеивание коммитов или объединеи всех коммитов в один [SQUASH]

[master]> git merge lesson3 - слияние ветки lesson3 c master

## отмена слияния из за конфликтов
git merge --abort

### Склеиваине коммитов SQUASH
1.[master]> git merge [моя ветка] --squash
##### Данная команда создаст файл в ветке master со всеми измениенями
2. [моя ветка]> git rebase HEAD~[3] # [от коммита HEAD объединям три ]параметр i - запуск в интерактивном режиме или автоматическом режиме
В удаленом перезаписать коммиты
git push --force

#%% md

#### Перенос отдельныйх коммитов [Chery Pick]
##### Перенести отдельный коммит с хешом {hash_commit}
[master]>git cherry-pick {hash_commit}
##### Перенести последний коммит ветки
[master]>git cherry-pick {branch}
##### Перенести все  коммит ветки
[master]>git cherry-pick ..{branch}

#%% md

#### Перезапсь коммита
##### добавит измение в последний коммит. Это будет другой коммит
Если вы хотите изменить только сообщение вашего последнего коммита, это очень просто:#%% md

## Базовае операции GIT в терминале BUSH

#%% md

### Базовае настройки Git
#### git config --global.user.name "[name]"  - указывается логин ,который будет записывать за каждым измением
#### git config --global.user.mail "[email-address]" - указание E-mail для связи с хозяином изменений
#### git config --global.core.editor "[program]" - указание текстового редактора по умолчанию
### Пример
>C:\Users\egor\GeekBrains\data_analitics>git config --global user.name
mikhailov_egor
>C:\Users\egor\GeekBrains\data_analitics>git config --global user.name "mikhailov_egor"

>C:\Users\egor\GeekBrains\data_analitics>git config --global user.email

>info@geekbrains.com
>C:\Users\egor\GeekBrains\data_analitics>git config --global user.email "ickzn@ya.ru"
>C:\Users\egor\GeekBrains\data_analitics>git config --list -все настройки

#%% md

### Создание нового репозитория как клон удвленного
На сайте github.com создаем новый репозитрий. После этого выходит инстукция
echo "# data_analitics" >> README.md
git clone it@github.com:barsuk2/data_analitics.git project - указание папки на лок компьютере

### Создание новый репозитория из локального
Создаем в github репозиторий second-site и и выполняем команды
git init
git add .
git commit -m "Initial commit"
git commit -am "Initial commit" - совместить add b commit
git remote add origin git@github.com:barsuk2/algorithms.git
git push -u origin master

### Указать, какой ключ использовать для этого репо
git config core.sshCommand 'ssh -i ~/.ssh/barsuk-git'
инфа попадет в .git/config
#%% md

### Клонирование репозитория
git clone it@github.com:barsuk2/data_analitics.git project - указание папки на лок компьютере

#%% md

### управление историей (коммитами)
##### Отображает измение с коммитами
>git log
##### Отображает измение с коммитами по всем веткам
>git log --all
>git log -2 # Двух последних
>git log --oneline # вывод в упращенном виде

##### Отображает все измениея в репозитории
>git reflog


### Лог из другой ветки можно изучить с помощью
git log имя_ветки
##### Восстановить истории коммитов до указанного
>git reset b84aea5

##### Удаляет изменения внесенные коммитом в  репозиторий. Создает новый коммит
>git revert b84aea5

##### Восстанавливает файл до предыдущего коммита
>git revert b84aea5
git restore b84aea5.txt

#%% md

#### Работа с ветками
##### Посмотреть список веток
>git branch

##### создать ветку
>git branch dev
##### создать ветку и перейти на нее
>git checkout -b feature

##### Создание новой ветки от мастер
>git branch dev-master master

##### Удаление ненужных веток
>git branch -d dev-master dev
##### Удаление ненужных веток на удаленном репо

git push origin -d remote_branch_name

#%% md

### Rebase измение места старта ветки
[no_master_branch]>git rebase master
git push --firse

#%% md

#### Версионирование
##### Установим последнему коммиту тег 1.0.0
>git tag 1.0.0
##### Посмотрим список тегов
>git tag --list

##### Загрузить теги на remote repository
>git push --tags
##### Удалить тег (для переноса на новое место)
git tag -d [-- delete]master_version

##### Удалить тег в remove repo(для переноса на новое место)
>git tag -d 1.0.1
>git push --delete origin 1.0.

#%% md

Сложные операции
1. Переключить ветку имея несохраненные измение [STASH]
2. склеивание коммитов или объединеи всех коммитов в один [SQUASH]
3. Перенос отдельныйх коммитов [Chery Pick]


#%% md

Переключить ветку имея несохраненные измение [STASH] спрятать
### Основные проблемы при работе с Git
##### Переключение веток при несохраненных данных
### Git STASH локальное пространство записывает все текущие измения
#### Перенесем несохраненные изменение в stash
>git stash
#### Просмотр пространства stash
>git stash list
#### После возврата на свою ветку вызываем из stash измения
>git stash pop stash@{1}
#### Дальше продолжаем вносить измениея или коммитим
>git stash push <file>
#### Можно добавить еще файлы в существующий stash

#%% md

2. склеивание коммитов или объединеи всех коммитов в один [SQUASH]

[master]> git merge lesson3 - слияние ветки lesson3 c master
### Склеиваине коммитов SQUASH
1.[master]> git merge [моя ветка] --squash
##### Данная команда создаст файл в ветке master со всеми измениенями
2. [моя ветка]> git rebase HEAD~[3] # [от коммита HEAD объединям три ]параметр i - запуск в интерактивном режиме или автоматическом режиме
В удаленом перезаписать коммиты
git push --force

#%% md

#### Перенос отдельныйх коммитов [Chery Pick]
##### Перенести отдельный коммит с хешом {hash_commit}
[master]>git cherry-pick {hash_commit}
##### Перенести последний коммит ветки
[master]>git cherry-pick {branch}
##### Перенести все  коммит ветки
[master]>git cherry-pick ..{branch}

#%% md

#### Перезапсь коммита
##### добавит измение в последний коммит. Это будет другой коммит
Если вы хотите изменить только сообщение вашего последнего коммита, это очень просто:😀️
>git commit --amend
##### Внести измниея в удаленный репо
>git push --force

#%% md

#### Решение конфликтов
26 мин
1.Удаляем вручном режиме все ненужное
2. git addamend
3. git commit

#%% md

### Fork это КОПИЯ репозитория другого разработчика
1. выбрать 'чужой' репо, сделать fork
 клонирование на локальный ПК
 Создать ветку от последнего commit
 Публиуация в свой удаленный репо
 pull request на репо 'чужой'

##### находим нужный репозиторий (https://github.com/AllenDowney/ThinkComplexity2Please type barsuk2/wer to confirm.), нажимаем

#%% md

### git reset или git revert
git reset отменяет коммит (ы) путём установки HEAD на другой коммит, а git revert путём создания нового коммита, который противоположен отменяемому.

В результате git reset с опцией --hard отменённые коммиты удаляются. Восстановить можно только плясками с бубном и в течение ограниченного промежутка времени.

git reset нужно делать, чтобы не оставлять мусор в истории, и если вы точно уверены, что вам не пригодится отменяемый коммит. И эту команду бесполезно выполнять локально, если коммит уже запушен в удалённый репозиторий

git revert во всех остальных случаях


>git commit --amend
##### Внести измниея в удаленный репо
>git push --force

#%% md

#### Решение конфликтов
26 мин
1.Удаляем вручном режиме все ненужное
2. git add
3. git commit

# удалить отслеживание
git rm --cached -r .idea/



#### Удалить не отслеживаемык файлы


Если вы его в игнор, используйте git clean -xf. Вы можете сделать git clean -df но это также удалит неотслеживаемые каталоги. Используйте -n для пробного прогона.
git clean -i -fd

### Fork это КОПИЯ репозитория другого разработчика
1. выбрать 'чужой' репо, сделать fork
 клонирование на локальный ПК
 Создать ветку от последнего commit
 Публиуация в свой удаленный репо
 pull request на репо 'чужой'

##### находим нужный репозиторий (https://github.com/AllenDowney/ThinkComplexity2Please type barsuk2/wer to confirm.), нажимаем

#%% md

### git reset или git revert

git reset visual/templates/admin/team/profile.html удалит из индекса файл добвленный add .

1. Если я хочу отменить все внесённые изменения и начать работу с чистого листа, я использую команду git reset --hard HEAD (самый частый случай
2. Я закомител в локале измения, хочу продолжить работу я использу git reset {{some-start-point-hash}}. git reset также откатит git add или git reset myfile.cpp выдернет только один файл

3. В локальной ветеке накопилось много коммитов, 9ae3b46e6 это последный коммит от мастера.
git reset --soft 9ae3b46e6 откатит все файлы до состояния git add . 
git reset 9ae3b46e6 откатит все файлы до  git add .

git reset отменяет коммит (ы) путём установки HEAD на другой коммит, а git revert путём создания нового коммита, который противоположен отменяемому.

В результате git reset с опцией --hard отменённые коммиты удаляются. Восстановить можно только плясками с бубном и в течение ограниченного промежутка времени.

git reset нужно делать, чтобы не оставлять мусор в истории, и если вы точно уверены, что вам не пригодится отменяемый коммит. И эту команду бесполезно выполнять локально, если коммит уже запушен в удалённый репозиторий

git revert во всех остальных случаях


    @app.template_filter('utcinlocal')
    def utcinlocal(utc_time, tz=None):
        time_zone = pytz.timezone(tz)
        if utc_time.tzinfo:
            return utc_time.astimezone(time_zone)
        else:
            return time_zone.localize(utc_time)

### Удаляем ветки: Локально и на origin
git branch -d feature/admin-tours-submenu -локально
git push -d origin feature/admin-tours-submenu -

### Удалить неотслеживаемые файлы

git clean -d -n -посмотреть, какие будут удалены
git clean -d -f - удалить


### Изменение названия коммита
Чтобы изменить имя последнего коммита, достаточно ввести:

git commit --amend -m "Новое название коммита"

Для изменения имени других коммитов, нужно сделать:

git commit --amend -c <commit ID>

и отредактировать имя коммита через редактор.

