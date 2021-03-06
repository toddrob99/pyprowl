#!/usr/bin/env python
"""
pyprowl is a Python module used to interface with the Prowl API.
Get more information about Prowl and generate your API key at http://prowlapp.com.
https://github.com/toddrob99/pyprowl

Example usage:

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
"""
__version__ = '3.0.1'

class Prowl:
    def __init__(self, apiKey="", appName="pyprowl"):
        self.apiKey = apiKey
        self.appName = appName

        # Define function aliases
        self.add = self.notify
        self.send = self.notify
        self.verify = self.verify_key

    def verify_key(self, apiKey=None):
        """
        verify_key(apiKey=None)
        
        apiKey = your Prowl API key - optional if provided at instantiation
        
        Returns a dictionary containing API response
        Raises an Exception if API call fails
        """
        if apiKey == None: apiKey=self.apiKey
        return self.api_call('verify',{'apikey':apiKey})

    def notify(self, event, description, priority=0, url=None, apiKey=None, appName=None):
        """
        notify(event, description, apiKey=None, priority=0, url=None, appName=None)
        
        event = string, title of the notification
        description = string, body of the description
        priority = int, optional, priority of the notification:
            -2 Very Low
            -1 Moderate
            0  Normal
            1  High
            2  Emergency
        url = string, optional, url to attach to the notification
        apiKey = API key to be used for the call - optional if provided at instantiation
        appName = string, name of app sending the notification - optional if provided at instantiation
        
        Returns a dictionary containing API response 
        Raises an Exception if API call fails
        """
        if appName == None: appName=self.appName
        if apiKey == None: apiKey=self.apiKey

        data = {'event':event, 'description':description, 'priority':priority, 
                'application':appName, 'apikey':apiKey}
        if url: data.update({'url':url})

        return self.api_call('add',data)

    def api_call(self, action, data={}):
        """
        api_call(action, data, apiKey=None)
        
        action = ['add','verify','retrieve_token','retrieve_apikey']
        data = dictionary containing data to be passed to Prowl - include apikey
        
        Returns a dictionary containing API response (see https://www.prowlapp.com/api.php#return)
        Raises an Exception if API call fails
        
        This function is usually not called directly. Instead use notify() or verify_key()
        """

        import requests
        try:
            import urllib.parse as Parse #python 3
        except:
            import urllib as Parse #python 2
        url = 'https://api.prowlapp.com/publicapi/'+action
        if action=='verify': url += "?"+Parse.urlencode(data)

        statusMessages = {   
                            '0'  : 'Connection error',
                            '-1' : 'Unknown error',
                            '200': 'Success',
                            '400': 'Bad request, the parameters you provided did not validate.',
                            '401': 'Not authorized, the API key given is not valid, and does not correspond to a user.',
                            '406': 'Not acceptable, your IP address has exceeded the API limit.',
                            '409': 'Not approved, the user has yet to approve your retrieve request.',
                            '500': 'Internal server error, something failed to execute properly on the Prowl side.'
                        }

        r = requests.post(url,data)
        if r.status_code != 200:
            response = {'status':'error', 'code':str(r.status_code), 'message':statusMessages.get(str(r.status_code),statusMessages['-1'])}
        else:
            response = r.content

        if isinstance(response,dict):
            if not response.get('errMsg',None): response.update({'errMsg':statusMessages[response.get('code')]})
        else:
            import xml.etree.ElementTree as ET
            root = ET.fromstring(response)
            child = root[0]
            response = {}
            response.update({'status':child.tag, 'message':child.text, 'errMsg':statusMessages[child.get('code')]})
            for key,val in list(child.attrib.items()):
                response.update({key:val})

        if response.get('status')=='success':
            return response
        else:
            raise Exception(response.get('code') + " " + response.get('message') + ": " + response.get('errMsg'))
