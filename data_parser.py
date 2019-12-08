

def parse_friends_dict(
        friendict,
        fields,
        separator=" |",
        default_fieldlen=15,
        remove_dead=False
        ):
    '''
    Converts response from get_friends_list to readable table <3

    '''
    res = ""
    line = ""
    equal_sign = ""
    for field in fields:
        line += make_entry(
                str(field),
                separator,
                calc_fieldlen(field, default_fieldlen))
    equal_sign += "="*(len(line))

    res += equal_sign + '\n'
    res += line + '\n'
    res += equal_sign + '\n'

    for friend in friendict['response']['items']:
        line = ""
        if not ('deactivated' in friend and remove_dead):
            for key in fields:
                line += parse_entry(key, friend, separator, default_fieldlen)
            res += line + '\n'
    res += equal_sign + '\n'
    return res


def calc_fieldlen(field, default_fieldlen):
    ynfields = ['sex', 'has_mobile', 'online']
    if field in ynfields:
        fieldlen = len(field)+1
    elif field == "city":
        fieldlen = 16
    elif field == "bdate":
        fieldlen = 11
    elif field in ['mobile_phone', 'home_phone']:
        fieldlen = 12
    elif field == "id":
        fieldlen = 11
    else:
        fieldlen = default_fieldlen
    return fieldlen


def parse_entry(
        key,
        user,
        separator,
        default_fieldlen):
    '''
    Retruns column part
    '''
    data = user_dict_to_data(user, key)
    fieldlen = calc_fieldlen(key, default_fieldlen)
    return make_entry(data, separator, fieldlen)


def make_entry(
        data,
        separator,
        fieldlen,
        ):
    return (("%"+str(fieldlen)+"s") % data + separator)


def user_dict_to_data(
        user,
        field
        ):
    '''
        Gets raw data to print
    '''
    data = ""
    if field == "sex":
        if user[field] == 2:
            data += "m"
        elif user[field] == 1:
            data += "f"
        else:
            data += "-"

    elif field == "has_mobile":
        if "has_mobile" in user:
            data += str(user["has_mobile"])
        else:
            data += "-"

    elif field == "city":
        if "city" in user:
            data = user["city"]["title"]
        else:
            data = "-"

    elif field == "contacts":
        if "mobile_phone" in user:
            data = user["mobile_phone"]
        elif "home_phone" in user:
            data = user["home_phone"]
        else:
            data = "-"
    else:
        # If no special case: first_name, last_name, id
        if field in user:
            data = str(user[field])
        else:
            data = "-"

    return data


def parse_person_dict(
        pdict,
        fields=["first_name", "last_name"]
        ):
    person = pdict["response"][0]
    res = ""
    for field in fields:
        res += str(person[field]) + " "
    return res


def parse_user_info(
        pdict,
        fields=["first_name", "last_name"]):
    res = ""
    person = pdict["response"][0]
    max_width = 0
    for field in fields:
        fieldlen = len(field)+1
        if fieldlen > max_width:
            max_width = fieldlen
    # Header
    res += "="*20 + '\n'

    res += make_entry("Name: ", "", max_width) + \
        str(person["first_name"]) + '\n'

    res += make_entry("Surname: ", "", max_width) + \
        str(person["last_name"]) + '\n'

    res += make_entry("uid: ", "", max_width) + \
        str(person["id"]) + '\n'

    res += "="*20 + '\n'

    # Requested info
    for field in fields:
        if field not in ['first_name', 'last_name', 'id']:
            res += ("%" + str(max_width) + "s") % str(field) + ": " + \
                   user_dict_to_data(person, field) + '\n'
    res += "="*20 + '\n'
    return res
