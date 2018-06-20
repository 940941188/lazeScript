# awk 'BEGIN{fs=" "} fs填入命令行分隔符号
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images | grep "^<none>" | awk 'BEGIN{fs=" "} {print $3}')
