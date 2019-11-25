'''
This is the python class to work with VK API:
    It has a private field, with which it is initialized - __token
    Token can be google'd and easily get. Check VK developers, it should
    be some kind of http request to get one.
'''
import requests


class VkApiClient:
    api_server = "https://api.vk.com/"
    api_version = "5.52"

    def get(self, what):
        # wrapper for requests
        # this makes you no need to add version and token manually
        url = VkApiClient.api_server + what + "&access_token=" + \
            self.__access_token + "&v=" + VkApiClient.api_version
        return requests.get(url)

    def check_token(self):
        # users.get=1, this is Pavel Durov, creator of VK and telegram.
        # if this test crashes, then the token is invalid.
        r = self.get('method/users.get?user_id=1').json()
        if r["error"]:
            pavel = False
        else:
            pavel = True
        return pavel

    def __init__(self, token, check=True):
        self.__access_token = token
        self.token_valid = self.check_token()
        if not self.token_valid:
            self.access_token = ""
            raise ValueError("Invalid token")
