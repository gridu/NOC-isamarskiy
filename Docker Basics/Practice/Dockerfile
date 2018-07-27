FROM java:8
EXPOSE 8080
ADD jenkins.war jenkins.war
RUN mkdir -p ~/.jenkins/plugins && \
        cd ~/.jenkins/plugins && \
        wget https://updates.jenkins.io/download/plugins/job-dsl/1.70/job-dsl.hpi && \
        wget https://updates.jenkins.io/download/plugins/structs/1.14/structs.hpi && \
        wget https://updates.jenkins.io/download/plugins/script-security/1.44/script-security.hpi 
         
ENTRYPOINT ["java","-jar","jenkins.war"]

