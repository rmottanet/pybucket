#!/usr/local/bin/python3.9
#-*- coding: UTF-8 -*-

import os
from app.config.load_environment import load_environment_variables
from app.handlers.repositories_handler import RepositoriesHandler
from app.display.error_display import display_error

username, app_password = load_environment_variables()


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
    try:
        
        handler = RepositoriesHandler(username, app_password)
        result = handler.edit_repository(workspace, repository_name, description, is_private)
        print(result)
        
    except Exception as e:
        display_error(e)
