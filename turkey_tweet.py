#!/usr/bin/python

import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages/')
import mraa
import time
from twython import Twython

# Authentication - Obtain Authorization URL
APP_KEY = 'lXZFwVtC8CGPKs4LOuv2m7WGS'
APP_SECRET = 'AoToSyNNyhzg2EhN38Edx6bQ59wPSLH8ztLZNZkWt1us7IzKUl'
OAUTH_TOKEN = '2892359329-fcC7F5l7Jx9CutiQACVrsTAUHN6GilG6RjmJPaH'
OAUTH_TOKEN_SECRET = '7HakyTT0SxwM8jAXjT8IPs73GW9QECRp3WnjUxXVNkmQZ'

twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


print (mraa.getVersion())
tempSensor = mraa.Aio(0)


thresholds ={
                    60: 'Guys, it is starting to get warm in here...',
                    80: 'Boys, do I smell good',
                   100: 'Yum time! @hello_techie'
                    }
while 1:
    temp = tempSensor.read() / 2.048
    print('Current Temperature: %.3fC' % temp)
    for thresholdTemp, thresholdMessage in thresholds.items():
                        if (temp > thresholdTemp):
                                            print thresholdMessage
                                            twitter.update_status(status='%.3fC: %s' % (temp, thresholdMessage))
                                            del thresholds[thresholdTemp]
    time.sleep(1)


