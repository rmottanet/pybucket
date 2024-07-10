#!/usr/local/bin/python3.9
#-*- coding: UTF-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from app.display.error_display import handle_adapter_response


class BitbucketAdapter:
    """
    This class handles interacting with the Bitbucket API.
    
    It provides methods for creating, deleting, and updating repositories
    on a Bitbucket account.
    """
    
    def __init__(self, username, app_password):
        """
        Initializes the BitbucketAdapter with the provided credentials.
    
        Args:
            username (str): The Bitbucket username.
            app_password (str): The Bitbucket app password.
        """
        self.auth = HTTPBasicAuth(username, app_password)
        self.base_url = 'https://api.bitbucket.org/2.0'
    
    def get_authenticated_session(self):
        """
        Creates a requests session object with pre-configured authentication.
    
        Returns:
            requests.Session: A session object authenticated with Bitbucket credentials.
        """
        session = requests.Session()
        session.auth = self.auth
        return session
    
    def create_repository(self, workspace, project, repo_name, description=None, is_private=True):
        """
        Creates a new repository on Bitbucket.
    
        Args:
            workspace (str): The Bitbucket workspace where the repository will be created.
            project (str): The Bitbucket project key associated with the repository.
            repo_name (str): The desired name for the new repository.
            description (str, optional): An optional description for the repository. Defaults to None.
            is_private (bool, optional): Specifies if the repository should be private (True) or public (False). Defaults to True.
    
        Returns:
            str: A message indicating success or failure with details.
        """
        session = self.get_authenticated_session()
        url = f'{self.base_url}/repositories/{workspace}/{repo_name}'
    
        # Define data for the POST request
        data = {
            'scm': 'git',  # Specify Git as the source control management system
            'is_private': is_private,
            'project': {
                'key': project
            }
        }
    
        # Include description if provided
        if description:
            data['description'] = description
    
        # Send a POST request to create the repository
        response = session.post(url, json=data)
    
        # Handle the response based on status code
        if response.status_code == 200:
            return f'{repo_name} repository successfully created.'
        else:
            # Provide error details in the response message
            #return f'Failure: {response.status_code} - {response.json()}'
            return handle_adapter_response(response)
    
    def delete_repository(self, workspace, repo_name):
        """
        Deletes a repository from Bitbucket.
    
        Args:
            workspace (str): The Bitbucket workspace where the repository resides.
            repo_name (str): The name of the repository to be deleted.
    
        Returns:
            str: A message indicating success or failure with details.
        """
        session = self.get_authenticated_session()
        url = f'{self.base_url}/repositories/{workspace}/{repo_name}'
    
        # Send a DELETE request to remove the repository
        response = session.delete(url)
    
        # Handle the response based on status code
        if response.status_code == 204:
            return f'{repo_name} repository successfully deleted.'
        else:
            # Provide error details in the response message
            #return f'Failure: {response.status_code} - {response.json()}'
            return handle_adapter_response(response)
    
    def update_repository(self, workspace, repo_name, description=None, is_private=None):
        """
        Updates a repository's description or privacy settings on Bitbucket.
        
        Args:
            workspace (str): The Bitbucket workspace where the repository resides.
            repo_name (str): The name of the repository to be updated.
            description (str, optional): An optional new description for the repository. Defaults to None (no change).
            is_private (bool, optional): An optional boolean to set the repository's privacy (True for private, False for public). Defaults to None (no change).
        
        Returns:
            str: A message indicating success or failure with details.
        """
        session = self.get_authenticated_session()
        url = f'{self.base_url}/repositories/{workspace}/{repo_name}'
        data = {}
        if description is not None:
            data['description'] = description
        if is_private is not None:
            data['is_private'] = is_private
        
        response = session.put(url, json=data)
        if response.status_code == 200:
            return f'{repo_name} repository successfully updated.'
        else:
            #return f'Failure: {response.status_code} - {response.json()}'
            return handle_adapter_response(response)
