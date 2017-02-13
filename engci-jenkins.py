#!/usr/bin/python
import jenkins

print('We are going inside jenkins')
server = jenkins.Jenkins('https://engci-private-blr.cisco.com/jenkins/ethan-blr/job/HIP/', username='aruthiya', password='David12#$')
print('We logged in jenkins')


# Copy a job
#print('We are going to copy the existing job')
#if server.job_exists('testjob'):
#  server.copy_job('testjob', 'empty_copy')
#print('We are going to enable job')
#server.enable_job('empty_copy')

# trigger job
print('We are going to trigger a empty job')
#server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)
server.build_job('empty_copy', parameters=None, token='goCD')

print('We are done')
