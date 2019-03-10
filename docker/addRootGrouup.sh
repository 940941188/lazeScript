user=$(whoami)
group=docker

creatGruop() {
  #create docker group if not exists
  egrep "^$group" /etc/group > /dev/null 2>&1;
  if [ $? -ne 0 ]
  then
    sudo groupadd -g 999 $group &&
    echo "create $group group success"
    return $?
  fi
  return 0
}

addUserToGroup() {
  sudo usermod -aG $group $user &&
  echo "$user add $group group success"
  return $?
}

creatGruop &&
addUserToGroup &&
sudo chmod a+rw /var/run/docker.sock &&
echo "sock add permission" &&
sudo systemctl restart docker &&
echo "restart docker server" &&
echo "ok."

