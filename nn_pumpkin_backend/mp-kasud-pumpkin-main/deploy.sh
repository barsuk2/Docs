#/bin/zsh
echo "Build image from source"
docker build . --platform=linux/amd64 -t kasud-backend-dummy:latest

echo "Saving the image"
docker save kasud-backend-dummy:latest | gzip > build/kasud-backend-dummy.tar.gz

echo "Transferring the image"
scp build/kasud-backend-dummy.tar.gz nn.proxy.dummy:artifacts/

echo "Unzip the image"
ssh nn.proxy.dummy -C "gunzip -c artifacts/kasud-backend-dummy.tar.gz | docker image load"

echo "Restart a container"
ssh nn.proxy.dummy -C "docker-compose -f kasud-backend-pumpkin/docker-compose.yaml down && docker-compose -f kasud-backend-pumpkin/docker-compose.yaml up -d"

echo "Delete old images"
ssh nn.proxy.dummy -C 'sudo docker rmi $(sudo docker images -f "dangling=true" -q)'
