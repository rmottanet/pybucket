#!/usr/local/bin/python3.9
#-*- coding: UTF-8 -*-

from app.adapters.bitbucket_adapter import BitbucketAdapter

class RepositoriesHandler:

    def __init__(self, username, app_password):
        self.bitbucket_adapter = BitbucketAdapter(username, app_password)

    def create_repository(self, workspace, project, repo_name, description=None, is_private=True):
        is_public = not is_private  # Convert is_private to is_public for clarity

        # Call BitbucketAdapter's create_repository with appropriate arguments
        return self.bitbucket_adapter.create_repository(workspace, project, repo_name, description, is_private)

    def delete_repository(self, workspace, repo_name):
        return self.bitbucket_adapter.delete_repository(workspace, repo_name)

    def edit_repository(self, workspace, repo_name, description=None, is_private=None):
        return self.bitbucket_adapter.update_repository(workspace, repo_name, description, is_private)
