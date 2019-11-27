#!/usr/bin/env python3
'''
This is a script for working with vicosin api_client,
application which you can use in another ones.

I remind you that vicosin is a tool for creating reports.
'''
import argparse
import sys
from api_client import VkApiClient

VERSION = "0.0.0"  # It can't be called a program as it doesn't do it's job

# Arguments check
parser = argparse.ArgumentParser()

# Optional arguments
parser.add_argument(
        "--friends",
        help="generate [userid]'s friends' list",
        action="store_true"
        )
parser.add_argument(
        "--test",
        help="check if access_token is valid",
        action="store_true"
        )
parser.add_argument(
        "--version",
        help="print version of VicosinTool and exit",
        action="store_true"
        )

parser.add_argument(
        "-v", "--verbose",
        help="add more text to output",
        action="store_true"
        )

# Positional arguments
if '--version' not in sys.argv:
    parser.add_argument(
            "access_token_file",
            help="path to access_token file",
            type=str
            )
    if '--test' not in sys.argv:
        parser.add_argument(
                "userid",
                help="id of a target",
                type=int
                )

args = parser.parse_args()

if args.version:
    print ("VicosinTool v" + VERSION + " by Quakumei.")
    exit()

# Read token
with open(args.access_token_file, 'r') as tokenfile:
    access_token = tokenfile.read().splitlines()[0]

# Some functions


def make_client(token, args):
    '''
    Creates a VkApiClient object and return it
    '''
    if args.verbose:
        print ("[...] Creating a client with following token: ", token)
        verb = True
    else:
        verb = False
    return VkApiClient(token, verb)


def test(access_token, args):
    '''
    Checks whether the token is good
    (VkApiClient raises an ValueError exception if token's bad)
    '''
    try:
        make_client(access_token, args)
    except ValueError:
        return False
    return True
# End of some functions


if args.test:
    if test(access_token, args):
        print("[+] Token's working good! owo")
    else:
        print("[-] Token's bad. unu")

else:
    if args.friends:
        client = make_client(access_token, args)

    print (args)
