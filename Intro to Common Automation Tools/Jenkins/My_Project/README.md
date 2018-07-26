Сервер 
18.222.169.10:8080 
#доступ для анонима включён
#если машина выключена, то её имя Igor_Master_Jenkins

Slave-агент 
13.58.130.106
#если машина выключена, то её имя Igor_Slave_Ansible

Репозиторий для проекта 
https://github.com/gagareg/jenkins

Trigger builds remotely 
http://18.222.169.10:8080/job/Mvn_Pipeline_second/build?token=123456
