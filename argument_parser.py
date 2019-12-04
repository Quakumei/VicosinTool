'''
Argument Parser for VicosinTool
'''

import argparse
import sys  # Maybe it's kinda lame


def parse_args():
    parser = argparse.ArgumentParser(
            description='VicosinTool - OSINT tool for Vk')

    user_id_required = not ('test' in sys.argv or
                            'help' in sys.argv or
                            'version' in sys.argv)
    access_token_required = not ('help' in sys.argv or
                                 'version' in sys.argv or
                                 '-tf' in sys.argv or
                                 '--token-file' in sys.argv)

    # Postional arguments: command, token, user_id
    parser.add_argument(
            "--command", "-c",
            type=str,
            required=True,
            help='''you know what does it mean'''
            )

    parser.add_argument(
            "--access_token", "-t",
            type=str,
            required=access_token_required,
            help='''access_token itself'''
            )
    parser.add_argument(
            "--user_id", "-T",
            type=int,
            required=user_id_required,
            help='''user_id of a target'''
            )

    # Optional positional arguments: --token_file
    parser.add_argument(
            "--token-file", "-tf",
            type=str,
            help='''path to file which contains token''',
            )

    parser.add_argument(
            "--column-separator", "-cs",
            type=str,
            help='''specify separator for the columns (default: |)'''
            )

    parser.add_argument(
            "--fields", "-f",
            type=str,
            help="specify fields for the command (default for 'friends'" +
            'command: "first_name,last_name,id")')

    # Optional arguments: --verbose --alive
    parser.add_argument(
            "--verbose", "-v",
            action="store_true",
            help="add more text to output"
            )

    parser.add_argument(
            "--alive", '-A',
            action="store_true",
            help="remove DELETED people from output"
            )

    return parser.parse_args()
