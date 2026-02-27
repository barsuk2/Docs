HostName 84.201.152.95 
User developer
    
    
Шаг 1. Сохранить ключ в файл macOS
nano ~/.ssh/nn_proxy
Шаг 2. Поставить правильные права (обязательно)
chmod 600 ~/.ssh/nn_proxy
Шаг 3. Подключиться вручную (проверка)
ssh -i ~/.ssh/nn_proxy developer@84.201.152.95
    
