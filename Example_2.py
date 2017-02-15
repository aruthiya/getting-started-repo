#!/usr/bin/python
import jenkins

print('We are going inside jenkins')
server = jenkins.Jenkins('https://engci-jenkins-rtp.cisco.com/jenkins/job/team_spvtg_carina/job/Debug/job/B/', username='aruthiya', password='David12#$')
print('We logged in jenkins')

# Copy a job
print('We are going to copy the existing job')
if server.job_exists('Metadata_SFS_POC'):
   server.copy_job('Metadata_SFS_POC', 'Metadata_SFS_POC_1')
print('We are going to enable job')
server.enable_job('Metadata_SFS_POC_1')

#jobs = server.get_jobs()
#print jobs

# trigger job
print('We are going to trigger a empty job')
server.build_job('Metadata_SFS_POC', parameters=None, token='eb6ccb5583324aef25ef605bb8c05c8a')
print('We are done')
