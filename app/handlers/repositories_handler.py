#!/usr/local/bin/python3.9
#-*- coding: UTF-8 -*-

from app.adapters.bitbucket_adapter import BitbucketAdapter

class RepositoriesHandler:
    """
    This class handles interacting with Bitbucket repositories through the BitbucketAdapter.

    It provides methods for creating, deleting, and editing repositories using the adapter's functionalities.
    """

    def __init__(self, username, app_password):
        """
        Initializes the RepositoriesHandler with the user's Bitbucket credentials.

        Args:
            username (str): The Bitbucket username.
            app_password (str): The Bitbucket app password.
        """
        self.bitbucket_adapter = BitbucketAdapter(username, app_password)

    def create_repository(self, workspace, project, repo_name, description=None, is_private=True):
        """
        Creates a new repository on Bitbucket.

        This method utilizes the BitbucketAdapter's `create_repository` function to perform the actual creation.
        It also converts the `is_private` flag to `is_public` for clarity when passing it to the adapter.

        Args:
            workspace (str): The Bitbucket workspace where the repository will be created.
            project (str): The Bitbucket project key associated with the repository.
            repo_name (str): The desired name for the new repository.
            description (str, optional): An optional description for the repository. Defaults to None.
            is_private (bool, optional): Specifies if the repository should be private (True) or public (False). Defaults to True.

        Returns:
            str: The message returned by the BitbucketAdapter, indicating success or failure with details.
        """
        is_public = not is_private  # Convert is_private to is_public for clarity

        # Call BitbucketAdapter's create_repository with appropriate arguments
        return self.bitbucket_adapter.create_repository(workspace, project, repo_name, description, is_private)

    def delete_repository(self, workspace, repo_name):
        """
        Deletes a repository from Bitbucket.

        This method delegates the deletion task to the BitbucketAdapter's `delete_repository` function.

        Args:
            workspace (str): The Bitbucket workspace where the repository resides.
            repo_name (str): The name of the repository to be deleted.

        Returns:
            str: The message returned by the BitbucketAdapter, indicating success or failure with details.
        """
        return self.bitbucket_adapter.delete_repository(workspace, repo_name)

    def edit_repository(self, workspace, repo_name, description=None, is_private=None):
        """
        Updates a repository's description or privacy settings on Bitbucket.

        This method leverages the BitbucketAdapter's `update_repository` function to handle the update.

        Args:
            workspace (str): The Bitbucket workspace where the repository resides.
            repo_name (str): The name of the repository to be updated.
            description (str, optional): An optional new description for the repository. Defaults to None (no change).
            is_private (bool, optional): An optional boolean to set the repository's privacy (True for private, False for public). Defaults to None (no change).

        Returns:
            str: The message returned by the BitbucketAdapter, indicating success or failure with details.
        """
        return self.bitbucket_adapter.update_repository(workspace, repo_name, description, is_private)
