'''
This is the python class to work with VK API:
    It has a private field, with which it is initialized - __token
    Token can be google'd and easily get. Check VK developers, it should
    be some kind of http request to get one.
'''
import requests


class VkApiClient:
    api_server = "https://api.vk.com/"

    def get(self, what, version):
        # wrapper for requests
        # this makes you no need to add version and token manually
        url = VkApiClient.api_server + what + "&access_token=" + \
            self.__access_token + "&v=" + version
        return requests.get(url)

    def check_token(self):
        # users.get=1, this is Pavel Durov, creator of VK and telegram.
        # if this test crashes, then the token is invalid.
        if self.verbosity:
            print("[...] Checking token...")
        version = '5.52'
        r = self.get('method/users.get?user_id=1', version).json()
        if 'error' in r:
            pavel = False
        else:
            pavel = True
        return pavel

    def get_friends_list(
            self,
            userid,
            fields_list=['city', 'domain', 'sex'],
            order='name'
            ):

        version = "5.103"
        fields = str(",".join(fields_list))

        r = self.get(
                "method/friends.get?user_id=" + str(userid) +
                "&order=" + order +
                "&fields=" + fields,
                version
                )
        return r.json()

    def __init__(self, token, verbosity=False, check=True):
        self.verbosity = verbosity
        self.__access_token = token
        self.token_valid = self.check_token()
        if not self.token_valid:
            self.access_token = ""
            raise ValueError("Invalid token")
