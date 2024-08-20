Установка Python 3.7 на Ubuntu
Обновите список пакетов и установите зависимости:

sh
Копировать код
sudo apt update
sudo apt install software-properties-common
Добавьте репозиторий для Python 3.7:

sh
Копировать код
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
Установите Python 3.7:

sh
Копировать код
sudo apt install python3.7
pip download --platform manylinux1_x86_64 --only-binary=:all: pytest


аг 1: Установка pytest и создание архива с зависимостями на машине с интернетом
Активируйте вашу виртуальную среду:

bash
Копировать код
source myenv/bin/activate
Создайте директорию для хранения пакетов:

bash
Копировать код
mkdir pytest-packages
Скачайте pytest и его зависимости:

bash
Копировать код
pip download pytest -d pytest-packages
Это скачает все необходимые файлы в директорию pytest-packages.

Заархивируйте директорию с пакетами:

bash
Копировать код
tar czvf pytest-packages.tar.gz pytest-packages
Теперь у вас есть архив pytest-packages.tar.gz, который содержит все необходимые файлы для установки pytest и его зависимостей.

Шаг 2: Перенос архива на машину без интернета
Скопируйте архив на машину без интернета. Вы можете использовать USB-накопитель или другой метод передачи файлов.

Разархивируйте архив на машине без интернета:

bash
Копировать код
tar xzvf pytest-packages.tar.gz
Шаг 3: Установка pytest на машине без интернета
Перейдите в разархивированную директорию:

bash
Копировать код
cd pytest-packages
Установите pytest и его зависимости из локальной директории:

bash
Копировать код
pip install --no-index --find-links=. pytest
Этот набор команд установит pytest и все его зависимости из локальной директории pytest-packages, не обращаясь к интернету.

Теперь pytest должен быть установлен и готов к использованию на машине без интернета. Вы можете проверить установку, активировав виртуальную среду и запустив pytest --version:

bash
Копировать код
source myenv/bin/activate
pytest --version
