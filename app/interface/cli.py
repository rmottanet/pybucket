#!/usr/local/bin/python3.9
#-*- coding: UTF-8 -*-

import os
import sys
import argparse

# Add project root directory to system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.config.load_environment import load_environment_variables
from app.display.error_display import display_error


def parse_arguments():
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


def bb_create_repo(repository_name, description=None, is_private=None, workspace=None, project=None):
    from app.handlers.repositories_handler import RepositoriesHandler
    
    try:
        
        if project is None:
            raise ValueError("Project ID is required for creating a new repository.")    
        handler = RepositoriesHandler(username, app_password)
        result = handler.create_repository(workspace, project, repository_name, description, is_private)
        print(result)
        
    except Exception as e:
        display_error(e)


def bb_delete_repo(repository_name, workspace=None):
    from app.handlers.repositories_handler import RepositoriesHandler

    try:
        
        handler = RepositoriesHandler(username, app_password)
        result = handler.delete_repository(workspace, repository_name)
        print(result)
        
    except Exception as e:
        display_error(e)


def bb_edit_repo(repository_name, workspace, description=None, is_private=None):
    from app.handlers.repositories_handler import RepositoriesHandler
    
    try:
        
        handler = RepositoriesHandler(username, app_password)
        result = handler.edit_repository(workspace, repository_name, description, is_private)
        print(result)
        
    except Exception as e:
        display_error(e)


if __name__ == "__main__":
    #app_password, username = load_environment_variables()
    load_environment_variables()
    app_password = os.getenv("BITBUCKET_APP_PASS")
    username = os.getenv("BITBUCKET_USER")

    # Parse command-line arguments
    args = parse_arguments()
        
    command_map = {
        "new": bb_create_repo,
        "delete": bb_delete_repo,
        "edit": bb_edit_repo
    }

    for command, function in command_map.items():
        if getattr(args, command):
            if command == "new":
                # Extract arguments for new command (considering optional description)
                # Se o comando for 'new', os argumentos são tratados como uma lista
                # O primeiro elemento é o nome do repositório e o segundo, se presente, é a descrição
                name = args.new[0]
                description = args.new[1] if len(args.new) > 1 else None
                is_private = args.public
                workspace = args.workspace
                project = args.project
                function(name, description=description, is_private=is_private, workspace=workspace, project=project)
            elif command == "delete":
                repository_name = args.delete[0]
                workspace = args.workspace
                function(repository_name, workspace=workspace)
            elif command == "edit":
                # Extract arguments for edit command (considering optional description and privacy)
                repository_name = args.edit[0]
                workspace = args.workspace
                description = None
                is_private = None
                for arg in args.edit[1:]:
                    if arg.startswith("--description="):
                        description = arg.split("=")[1]
                    elif arg == "--public":
                        is_private = False
                function(repository_name, workspace, description, is_private)
            break
