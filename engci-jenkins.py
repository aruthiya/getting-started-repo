import jenkins
import time
import json
import random

jobName = 'E2E-Jenkins-GoCD-Test'
fullJobName = 'team_spvss-advdev/'+jobName
jobToken = 'goCD'
genUser = 'advdev-cloud.gen'
genPassword = 'adcg:c1sc0:04'
server = jenkins.Jenkins('https://engci-private-blr.cisco.com/jenkins/', username='aruthiya', password='A1b2c3d4$%^&')

def waitJobQueue() :
    while server.get_queue_info():
        print('Waiting for job queue ...')
        time.sleep(random.uniform(1,10))


def waitJob2Complete(job_name, job_number) :
    while True:
        time.sleep(1)
        job_info = server.get_job_info(job_name)
        print('Wait for job_number:'+str(job_number) +' to completion ... [lastCompletedBuild:'+ str(job_info['lastCompletedBuild']['number'])+']')
        if job_info['lastCompletedBuild']['number'] >= job_number :
            break;
        elif job_info['color'] != 'blue_anime' and job_info['lastCompletedBuild']['number'] >= job_number :
            break;


if server.job_exists(fullJobName):
    print('Check job queue ...')
    waitJobQueue()

    job_info = server.get_job_info(fullJobName)
    jobNumber = job_info['nextBuildNumber']

    print('Trigger job_number:'+str(jobNumber))
    runJob = server.build_job(fullJobName, parameters=None, token=jobToken)
    waitJob2Complete(fullJobName, jobNumber)

    print('\nConsole output:')
    print server.get_build_console_output(fullJobName, jobNumber)

    build_info = server.get_build_info(fullJobName, jobNumber)
    print('Build result: '+build_info['result'])

else:
    print('Job named {0} does not exist !!'.format(fullJobName))
