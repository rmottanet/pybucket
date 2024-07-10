#!/usr/local/bin/python3.9
#-*- coding: UTF-8 -*-

import os
import sys
from dotenv import load_dotenv


def load_environment_variables():
    """
    Load BitBucket app password from .env file, system keychain, or prompt user.
    
    Try in this order:
    1. .env file.
    2. System.
    3. User input.
    """
    # Construct path to .env file.
    dotenv_path = os.path.join(os.path.dirname(__file__), '../..', '.env')
    
    # Load .env from path.
    load_dotenv(dotenv_path)
    
    # Try get variables from environment.
    app_password = os.environ.get('BITBUCKET_APP_PASS')
    username = os.environ.get('BITBUCKET_USER')
    
    # If not find the variables prompt it.    
    if app_password is None or username is None:
        # Prompt.
        app_password = input("Insert an app password: ")
        username = input("Insert bitbucket user name: ")
        # Add a new environment variable
        os.environ["BITBUCKET_APP_PASS"] = app_password
        os.environ["BITBUCKET_USER"] = username
