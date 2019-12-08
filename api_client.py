import requests


class VkApiClient:
    '''
    Class for making requests to vk.com API
    using users access_token
    '''
    api_server = "https://api.vk.com/"

    def get(
            self,
            request,
            version
            ):
        '''
        Makes get request and returns raw response.
        Wrapper for get requests.
        '''
        url = VkApiClient.api_server + request + \
            "&access_token=" + self.__access_token + \
            "&v=" + version
        return requests.get(url)

    def check_token(self):
        '''
        return True if token is valid
        '''
        response = self.get_user(1)
        return not ('error' in response)

    def get_friends(
            self,
            userid,
            fields_list=['domain', 'sex'],
            order='name'
            ):
        '''
        Returns json formatted list of friends
        of user specified.
        '''
        version = "5.103"
        fields = str(",".join(fields_list))

        request = "method/friends.get?" + \
            "user_id=" + str(userid) + \
            "&order=" + order + \
            "&fields=" + fields

        response = self.get(
                request,
                version
                )
        return response.json()

    def get_user(
            self,
            userid,
            fields=['first_name', 'last_name', 'id']
            ):
        version = "5.52"
        if userid != "":
            r = self.get(
                    "method/users.get" +
                    "?user_id=" + str(userid) +
                    "&fields=" + ",".join(fields),
                    version
                    )
        else:
            r = self.get(
                    "method/users.get" +
                    "?fields=" + ",".join(fields),
                    version
                    )

        return r.json()

    def get_chat(
            self,
            chat_id,
            fields=[]):
        version = "5.103"
        if fields != []:
            r = self.get(
                    "method/messages.getChat" +
                    "?chat_id=" + str(chat_id) +
                    "&fields=" + ",".join(fields),
                    version
                    )
        else:
            r = self.get(
                    "method/messages.getChat" +
                    "?chat_id=" + str(chat_id),
                    version
                    )
        print(r.json())
        return r.json()

    def __init__(
            self,
            access_token,
            options=[]  # specify options with words\letters
            ):
        # TODO change behaviour depending on options

        self.__access_token = access_token
        self.__options = options
        # Token check
        if not self.check_token():
            self.access_token = ""
            raise ValueError("Invalid token")
