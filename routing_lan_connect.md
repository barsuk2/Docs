
определить ip
dig +short hvgw02.nornik.ru

добавить в роутинг
sudo ip route add 91.209.147.0/24 via 192.168.1.1 dev enp3s0
sudo nano /etc/network/interfaces
auto enp3s0
iface enp3s0 inet dhcp
    post-up ip route add 91.209.147.0/24 via 192.168.1.1 dev enp3s0


