#!/usr/bin/env python

"""
Example usage of pyprowl module
"""

import pyprowl

p = pyprowl.Prowl('YOUR_PROWL_API_KEY')

try:
    p.verify_key()
    print("Prowl API key successfully verified!")
except Exception as e:
    print("Error verifying Prowl API key: {}".format(e))
    exit()

try:
    p.notify(event='Event name', description='Description of event', 
             priority=0, url='http://www.example.com', 
             #apiKey='uncomment and add API KEY here if different', 
             appName='Name of app sending the notification')
    print("Notification successfully sent to Prowl!")
except Exception as e:
    print("Error sending notification to Prowl: {}".format(e))
