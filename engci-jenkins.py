#!/usr/bin/python
import jenkins

print('We are going inside jenkins')
server = jenkins.Jenkins('https://engci-private-blr.cisco.com/jenkins/ethan-blr/job/HIP/', username='aruthiya', password='David12#$')
print('We logged in jenkins')

# Copy a job
print('We are going to copy the existing job')
if server.job_exists('testjob'):
  server.copy_job('testjob', 'empty_copy')
print('We are going to enable job')
server.enable_job('empty_copy')
print('We are done')
