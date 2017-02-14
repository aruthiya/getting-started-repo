#!/usr/bin/python

import json 
import sys
import urllib2
import base64

user = 'aruthiya'
password = 'David12#$'
#jenkinsUrl = 'https://engci-jenkins-rtp.cisco.com/jenkins/job/team_spvtg_carina/job/Debug/job/B/job/Metadata_SFS_POC/lastBuild/api/json'
jenkinsUrl = 'https://engci-private-blr.cisco.com/jenkins/ethan-blr/job/HIP/job/testjob_1//lastBuild/api/json'
jobName = 'Metadata_SFS_POC'

def urlopen(url, data=None):
    '''Open a URL using the urllib2 opener.'''
    print "URL : " + url
    request = urllib2.Request(url, data)
    base64string = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    response = urllib2.urlopen(request)
    return response

try:
    jenkinsStream   = urlopen(jenkinsUrl)
except urllib2.HTTPError, e:
    print "URL Error: " + str(e.code) 
    print "      (job name [" + jobName + "] probably wrong)"
    sys.exit(2)

try:
    buildStatusJson = json.load( jenkinsStream )
except:
    print "Failed to parse json"
    sys.exit(3)

if buildStatusJson.has_key( "result" ):      
    print "[" + jobName + " #" + str(buildStatusJson["number"]) + "]: " + buildStatusJson["result"] 
    if buildStatusJson["result"] != "SUCCESS" :
		#exit(4)
		return FAIL
else:
	sys.exit(5)

sys.exit(0)
