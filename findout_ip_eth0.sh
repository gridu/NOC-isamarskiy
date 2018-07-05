ifconfig eth0| grep 'inet addr:' | awk '{print$1$2}'
