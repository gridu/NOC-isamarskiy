ID_DOCKER=$(sudo docker ps | grep gagareg/jenkins_with_dsl_plugin:2_1 |awk '{print $1}')
sudo docker exec -it $ID_DOCKER cat /root/.jenkins/secrets/initialAdminPassword

