import api_client


class VicosinProcessor:
    '''
    Class for working with api_client
    '''
    def __init__(self, args):
        self.args = args
        self.access_token = self.get_token()

    def make_client(self, access_token=""):
        '''
        Creates VkApiClient object and return it
        '''
        if access_token == "":
            access_token = self.access_token

        # Get options from arguments
        options = []
        if self.args.verbose:
            options += "verbose"

        client = api_client.VkApiClient(
                access_token,
                options)
        return client

    def check_token(
            self,
            access_token="null"):
        '''
        Returns True if token's good
        '''
        if access_token == 'null':
            access_token = self.access_token
        try:
            self.make_client(access_token)
        except ValueError:
            return False
        return True

    def get_token(self):
        '''
        Return token or "" if not specified
        '''
        if self.args.access_token:
            access_token = self.args.access_token
        elif self.args.token_file:
            with open(self.args.token_file, 'r') as tokenfile:
                access_token = tokenfile.read().splitlines()[0]
        else:
            access_token = ""
        return access_token

    def get_user(
            self,
            user_id,
            fields=[]
            ):
        '''
        Returns info dict about user
        '''
        if user_id != "":
            return self.make_client().get_user(user_id, fields)
        else:
            return self.make_client().get_user("", fields)

    def get_friends(
            self,
            user_id,
            fields=['first_name', 'last_name', 'id']
            ):
        '''
        Returns dict of friends of user_id
        '''
        return self.make_client().get_friends(user_id, fields)

    def get_chat_info(
            self,
            chat_id,
            ):
        '''
        messages.getChat implementation
        '''
        return self.make_client().get_chat(chat_id)

    def get_chat_users(
            self,
            chat_id,
            fields=["id"]):
        '''
        messages.getChat which returns info on chat users
        '''
        return self.make_client().get_chat(chat_id, fields)
