#!/usr/bin/python
import jenkins

print('We are going inside jenkins')
server = jenkins.Jenkins('https://engci-private-blr.cisco.com/jenkins/ethan-blr/job/HIP/', username='aruthiya', password='David12#$')
print('We logged in jenkins')

# Copy a job
print('We are going to copy the existing job')
if server.job_exists('testjob'):
   server.copy_job('testjob', 'testjob_1')
print('We are going to enable job')
server.enable_job('testjob_1')

#jobs = server.get_jobs()
#print jobs

# trigger job
#print('We are going to trigger a empty job')
#server.build_job('empty_copy', parameters=None, token='ecea623de363e1f3068890231772bf8b')
print('We are done')
