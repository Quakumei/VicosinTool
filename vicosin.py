#!/usr/bin/env python3
'''
VicosinTool CLI interface
'''
import data_parser
import argument_parser
import vicosin_processor

VERSION = "0.0.1"

# Get arguments: command, token, user_id + options
args = argument_parser.parse_args()

processor = vicosin_processor.VicosinProcessor(args)

access_token = processor.get_token()

# Command processing
command = args.command
if command == 'version':
    '''
        Display tool info and exit.
    '''
    print(VERSION)

elif command == 'help':
    '''
        Display help to get help.
    '''
    help_message = "run ./vicosin.py -h"
    print(help_message)

elif command == 'test':
    '''
        Check validity of a token.
    '''
    if processor.check_token(access_token):
        print("+")
    else:
        print("-")

elif command == 'friends':
    '''
        List friends with specified fields and separator.
    '''
    # Defaults
    DEFAULT_SEPARATOR = " |"
    DEFAULT_FIELDS = ['first_name', 'last_name', 'id']

    # Get output format data from args
    if args.column_separator:
        separator = args.column_separator
    else:
        separator = DEFAULT_SEPARATOR

    if args.fields:
        fields = args.fields.split(",")
    else:
        fields = DEFAULT_FIELDS

    if args.alive:
        alive = True
    else:
        alive = False

    # Get data
    person_dict = processor.get_user(args.user_id)
    friends_dict = processor.get_friends(args.user_id, fields)

    # Convert response
    person_out = data_parser.parse_person_dict(
            person_dict,
            ["first_name", "last_name", "id"]
            )
    friends_out = data_parser.parse_friends_dict(
            friends_dict,
            fields=fields,
            separator=separator,
            remove_dead=alive
            )
    print(person_out)
    print(friends_out)

elif command == "profile":
    if args.fields:
        fields = args.fields.split(",")
    else:
        fields = ['first_name', 'last_name', 'id']
    person_dict = processor.get_user(args.user_id, fields)
    person_out = data_parser.parse_user_info(person_dict, fields)
    print(person_out)

elif command == "chatlist":
    me = processor.get_user("", ["first_name", "last_name"])
    me_out = data_parser.parse_user_info(me)

    print(me_out)
    # Rewrite this part later please
    print("#\tTitle")
    for i in range(1, 1000000):
        chat = processor.get_chat_info(i)
        chat_info = chat["response"]
        print("%4s" % chat_info["id"] + '\t' + "%20s" % chat_info["title"])

    print("="*28)
    exit()

elif command == "chat":
    pass

else:
    print("Unknown command")

exit()
