'''
This is the python class to work with VK API:
    It has a private field, with which it is initialized - __token
    Token can be google'd and easily get. Check VK developers, it should
    be some kind of http request to get one.
'''


class VkApiClient:
    def __init__(self, token):
        self.__token = token
