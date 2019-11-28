

def FriendsDictToTable(
        friendict,
        fields=['first_name', 'last_name', 'id'],
        separator="|"
        ):
    '''
    Converts response from get_friends_list to readable table <3

    '''
    # TODO get rid of odd \t in the end of each line
    res = ""
    line = ""
    equal_sign = ""
    for field in fields:
        line += ("%15s" % str(field) + separator)
        equal_sign += "="*16

    res += equal_sign + '\n'
    res += line + '\n'
    res += equal_sign + '\n'

    for friend in friendict['response']['items']:
        line = ""
        for key in fields:
            line += ("%15s" % str(friend[key]) + separator)
        res += line + '\n'
    return res


def DictToFirstLastName(json):
    a = json["response"][0]
    first = a["first_name"]
    last = a["last_name"]
    return first + ' ' + last
