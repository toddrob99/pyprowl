#!/usr/bin/env python

"""
Example usage of pyprowl module
"""

import pyprowl

p = pyprowl.Prowl('YOUR_PROWL_API_KEY')

try:
    result = p.verify_key()
    print "Prowl API key successfully verified!"
except Exception, e:
    print "Error verifying Prowl API key:",e
    exit()

try:
    p.notify('Event name', 'Description of event', 
             priority=0, url='http://www.example.com', appName='Name of app sending the notification')
    print "Notification successfully sent to Prowl!"
except Exception, e:
    print "Error sending notification to Prowl:",e
