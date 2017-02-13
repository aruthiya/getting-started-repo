#!/usr/bin/python
import jenkins
import os

print('We are going inside jenkins')
server = jenkins.Jenkins('https://engci-private-blr.cisco.com/jenkins/ethan-blr/job/HIP/', username='aruthiya', password='David12#$')
print('We logged in jenkins')

