method="${1}";
case ${method} in
  -o) 
    sudo mkdir -p /etc/docker;
    sudo tee /etc/docker/daemon.json << EOF
{}
EOF

    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ;;
  -a) 
    sudo mkdir -p /etc/docker;
    sudo tee /etc/docker/daemon.json << EOF
{
  "registry-mirrors": ["https://r53k1kg3.mirror.aliyuncs.com"]
}
EOF

    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ;;
  *)
    echo "`basename ${0}`:usage: [-o origion] | [-a aliyuncs mirror ]"
    exit 1 # Command to come out of the program with status 1
    ;;
esac
