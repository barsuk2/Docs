### Необходимо сменить ip для сети docker
1. ip a - выводим все сети на сервере. Среди них находим нужную докер сеть. 
2. docker network ls ищем сеть docker
3. docker network inspect <имя сети> исследуем нужню сеть
### Решение
1. docker network create --subnet=192.168.100.0/24 my_custom_network - режим создания сети вручную
2. В docker-compose.yml меняем конфигурацию
networks:
  my_custom_network:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.100.0/24
          gateway: 192.168.100.1


### очистить
docker-compose down # Останавливает и удаляет все контейнеры, сети и тома, определенные в вашем docker-compose.yml
docker system prune -f № Удаляет неиспользуемые Docker объекты
sudo systemctl restart docker
