# pyprowl
Python module for sending Prowl notifications
Created by Todd Roberts
https://github.com/toddrob99/pyprowl

## Usage

	import pyprowl

	p = pyprowl.Prowl('YOUR_PROWL_API_KEY')

	try:
		p.verify_key()
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

## Changelog

### v1.0
* Supports verification of API key and sending of notifications
* API key can be set at instantiation and left out of subsequent calls, or it can be set on each call
* App name can be set at instantiation and left out of subsequent calls, or it can be set on each call to notify()
