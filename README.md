# pyprowl

Python module for sending Prowl notifications

Created by Todd Roberts

https://github.com/toddrob99/pyprowl

## Usage

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

## Changelog

### v3.0.0
* Added support for python 3 using requests module

### v1.0.2
* Fixed package layout (moved code from `pyprowl.py` to `__init__.py` to support importing of module)

### v1.0.1
* Updated package layout for submission to PyPI

### v1.0
* Supports verification of API key and sending of notifications
* API key can be set at instantiation and left out of subsequent calls, or it can be set on each call
* App name can be set at instantiation and left out of subsequent calls, or it can be set on each call to notify()
