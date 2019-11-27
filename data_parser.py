

def FriendsDictToTable(
        friendict,
        fields=['first_name', 'last_name', 'id'],
        params=[]
        ):
    '''
    Converts response from get_friends_list to readable table <3

    '''
    # TODO get rid of odd \t in the end of each line
    res = ""
    line = ""
    for field in fields:
        line += ("%10s" % str(field)+'\t')
    res += line + '\n'

    for friend in friendict['response']['items']:
        line = ""
        for key in fields:
            line += ("%10s" % str(friend[key])+'\t')
        res += line + '\n'
    return res
