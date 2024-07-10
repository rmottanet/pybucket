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


def bb_create_repo(repository_name, description=None, is_private=None, workspace=None, project=None):
    """
    Creates a new BitBucket repository.

    This function handles creating a new repository by:
        * Validating that the `project` argument is provided (required for creating new repositories).
        * Creating a `RepositoriesHandler` instance to interact with BitBucket.
        * Calling the `create_repository` method of the handler to perform the creation.
        * Printing the success or error message returned by the handler.

    Args:
        repository_name (str): The desired name for the new repository.
        description (str, optional): An optional description for the repository. Defaults to None.
        is_private (bool, optional): Specifies if the repository should be private (True) or public (False). Defaults to True.
        workspace (str, optional): The Bitbucket workspace where the repository will be created. Defaults to None.
        project (str, optional): The Bitbucket project key associated with the repository (required).
    """
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
    """
    Deletes a BitBucket repository.

    This function handles deleting a repository by:
        * Creating a `RepositoriesHandler` instance to interact with BitBucket.
        * Calling the `delete_repository` method of the handler to perform the deletion.
        * Printing the success or error message returned by the handler.

    Args:
        repository_name (str): The name of the repository to be deleted.
        workspace (str, optional): The Bitbucket workspace where the repository resides. Defaults to None.
    """
    from app.handlers.repositories_handler import RepositoriesHandler

    try:
        
        handler = RepositoriesHandler(username, app_password)
        result = handler.delete_repository(workspace, repository_name)
        print(result)
        
    except Exception as e:
        display_error(e)


def bb_edit_repo(repository_name, workspace, description=None, is_private=None):
    """
    Edits a BitBucket repository.

    This function handles editing a repository by:
        * Creating a `RepositoriesHandler` instance to interact with BitBucket.
        * Calling the `edit_repository` method of the handler to perform the update.
        * Printing the success or error message returned by the handler.

    Args:
        repository_name (str): The name of the repository to be edited.
        workspace (str): The Bitbucket workspace where the repository resides.
        description (str, optional): An optional new description for the repository. Defaults to None (no change).
        is_private (bool, optional): An optional boolean to set the repository's privacy (True for private, False for public). Defaults to None (no change).
    """
    from app.handlers.repositories_handler import RepositoriesHandler
    
    try:
        
        handler = RepositoriesHandler(username, app_password)
        result = handler.edit_repository(workspace, repository_name, description, is_private)
        print(result)
        
    except Exception as e:
        display_error(e)


if __name__ == "__main__":
    """
    Main execution block.

    This block performs the following steps:
        1. Loads environment variables containing username and app password.
        2. Parses command-line arguments using `parse_arguments`.
        3. Creates a dictionary mapping commands to their respective functions (`bb_create_repo`, `bb_delete_repo`, `bb_edit_repo`).
        4. Iterates over the command map and executes the corresponding function based on the provided command.
            * For the `new` command, it extracts arguments considering the possibility of an optional description.
            * For the `delete` command, it extracts the repository name and workspace.
            * For the `edit` command, it extracts arguments considering optional description and privacy flags.
    """
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
