

def parse_friends_dict(
        friendict,
        fields=['first_name', 'last_name', 'id'],
        separator="|"
        ):
    '''
    Converts response from get_friends_list to readable table <3

    '''
    res = ""
    line = ""
    equal_sign = ""
    for field in fields:
        line += ("%15s" % str(field) + separator)
        equal_sign += "="*(15+len(separator))

    res += equal_sign + '\n'
    res += line + '\n'
    res += equal_sign + '\n'

    for friend in friendict['response']['items']:
        line = ""
        for key in fields:
            if key == "sex":
                if friend[key] == 2:
                    line += ("%15s" % "male" + separator)
                elif friend[key] == 1:
                    line += ("%15s" % "female" + separator)
                else:
                    line += ("%15s" % "dafuq" + separator)
            elif key == "has_mobile":
                if "has_mobile" in friend:
                    line += ("%15s" % "1" + separator)
                else:
                    line += ("%15s" % "NaN" + separator)
            else:
                if key in friend:
                    line += ("%15s" % str(friend[key]) + separator)
                else:
                    line += ("%15s" % "null" + separator)
        res += line + '\n'
    return res


def parse_person_dict(
        pdict,
        fields=["first_name", "last_name"]
        ):
    person = pdict["response"][0]
    res = ""
    for field in fields:
        res += str(person[field]) + " "
    return res
