#!/usr/bin/env python3
'''
VicosinTool CLI interface
'''
import api_client
import data_parser
import argument_parser
import vicosin_processor

VERSION = "0.0.1"

# Get arguments: command, token, user_id + options
args = argument_parser.parse_args()

processor = vicosin_processor.VicosinProcessor(args)

access_token = processor.get_token()

# Command processing
if args.command == 'version':
    print(VERSION)
    exit()

elif args.command == 'test':
    if processor.check_token(access_token):
        print("+")
    else:
        print("-")
    exit()
