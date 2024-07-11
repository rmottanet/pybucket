#!/usr/local/bin/python3.9
#-*- coding: UTF-8 -*-

import argparse


def parse_arguments():
    """
    Parses command-line arguments using argparse.

    This function defines the arguments accepted by the PyBucket CLI tool and returns a namespace object containing the parsed arguments.

    Returns:
        argparse.Namespace: An object containing parsed arguments.
    """
    
    parser = argparse.ArgumentParser(
        description='PyBucket - A tiny BitBucket CLI.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Repository management subcommands
    parser.add_argument(
        "-n", "--new", nargs="+",
        help="Create a new repository on BitBucket.\n"
             "Usage: -n REPO_NAME [DESCRIPTION] --project <project_id> --workspace <workspace_name>"
    )
    
    parser.add_argument(
        "-d", "--delete", nargs="+",
        help="Deletes a repository on BitBucket.\n"
             "Usage: -d REPO_NAME --workspace <workspace_name>"
    )
    
    parser.add_argument(
        "-e", "--edit", nargs="+",
        help="Edit a repository on BitBucket.\n"
             "Usage: -e REPO_NAME [--description NEW_DESCRIPTION] [--public]"
    )
    
    # Required global parameters
    parser.add_argument(
        "--workspace", required=True,
        help="Bitbucket Workspace Name"
    )
    
    parser.add_argument(
        "--project",
        help="Bitbucket Project Id"
    )
    
    parser.add_argument(
        "--public", action='store_false',
        help="Specify if the repository should be public"
    )
    
    return parser.parse_args()
