#!/usr/bin/python
import jenkins
import time
import json
import random


server = jenkins.Jenkins('https://engci-private-blr.cisco.com/jenkins/ethan-blr/job/HIP/', username='aruthiya', password='A1b2c3d4$%^&')

# Create a new job
if not server.job_exists('empty_hip'):
    server.create_job('empty_hip', jenkins.EMPTY_CONFIG_XML)
server.disable_job('empty_hip')
