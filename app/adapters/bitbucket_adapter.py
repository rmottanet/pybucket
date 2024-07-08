#!/usr/local/bin/python3.9
#-*- coding: UTF-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from app.display.error_display import handle_adapter_response


class BitbucketAdapter:
    
    def __init__(self, username, app_password):
        self.auth = HTTPBasicAuth(username, app_password)
        self.base_url = 'https://api.bitbucket.org/2.0'
    
    def get_authenticated_session(self):
        session = requests.Session()
        session.auth = self.auth
        return session
    
    def create_repository(self, workspace, project, repo_name, description=None, is_private=True):
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
