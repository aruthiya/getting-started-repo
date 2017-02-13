#!/usr/bin/python
import jenkins
import os

print('We are going inside jenkins')
server = jenkins.Jenkins('https://engci-private-blr.cisco.com/jenkins/ethan-blr/job/HIP/', username='aruthiya', password='David12#$')

# Create a new job
if not server.job_exists('empty'):
    server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
