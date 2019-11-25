'''
This is the python class to work with VK API:
    It has a private field, with which it is initialized - __token
    Token can be google'd and easily get. Check VK developers, it should
    be some kind of http request to get one.
'''
import requests


class VkApiClient:
    api_server = "https://api.vk.com"
    def __init__(self, token):
        self.__token = token
    
    def check_token(self):
        user_id = 1 # it can be only int
        api_version = "5.52" # idk if it can be another
        req = "methods/users.get?user_id="+user_id+"&v="+api_version+"&access_token="+self.__token
        #rewrite this part, make no duplication of access_token, put request into another functions
        r = requests.get(VkApiClient.api_server+req)
        r = r.json()
        if r['response']['first_name']=="Pavel" and ['response']['last_name']=="Durov":
            return True
        else:
            return False
