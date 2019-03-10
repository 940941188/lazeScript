method="${1}";
url=socks5://127.0.0.1:1083

case ${method} in
  -o)
    git config --global http.proxy $url
    git config --global https.proxy $url
    git config --global http.sslVerify false
    echo 'git ss opene'
    ;;
  -c)
    git config --global --unset http.proxy
    git config --global --unset https.proxy
    echo 'git ss closed'
    ;;
  *)
    echo "`basename ${0}`:usage: [-o ss open] | [-c ss close]"
    exit 1 # Command to come out of the program with status 1
    ;;
esac
