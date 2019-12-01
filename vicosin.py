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
    print(VERSION)

elif command == 'help':
    print("run ./vicosin.py -h")

elif command == 'test':
    if processor.check_token(access_token):
        print("+")
    else:
        print("-")
elif command == 'friends':
    person_dict = processor.get_user(args.user_id)
    friends_dict = processor.get_friends(args.user_id)

    person_out = data_parser.parse_person_dict(
            person_dict,
            ["first_name", "last_name", "id"]
            )
    friends_out = data_parser.parse_friends_dict(
            friends_dict,
            # fields=default,
            # separator=default
            )
    print(person_out)
    print(friends_out)


else:
    print("Unknown command")

exit()
