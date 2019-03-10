method="${1}";
case ${method} in
  -o) 
    yarn config set registry 'https://registry.yarnpkg.com';
    ;;
  -t) 
    yarn config set registry 'https://registry.npm.taobao.org';
    ;;
  *)
    echo "`basename ${0}`:usage: [-o origion] | [-t taobao]"
    exit 1 # Command to come out of the program with status 1
    ;;
esac
