import jenkins
import time
import json
import random


server = jenkins.Jenkins('https://engci-jenkins-rtp.cisco.com/jenkins/', username='aruthiya', password='A1b2c3d4$%^&')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
