#!/usr/bin/python
import jenkins



server = jenkins.Jenkins('https://engci-private-blr.cisco.com/jenkins/ethan-blr/job/HIP/', username='aruthiya', password='A1b2c3d4$%^&')

# Create a new job
if not server.job_exists('empty'):
    server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
