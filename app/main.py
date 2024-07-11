#!/usr/local/bin/python3.9
#-*- coding: UTF-8 -*-

import os
import sys

# Add project root directory to system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import app.interface as cli


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
    # Parse command-line arguments
    args = cli.parse_arguments()
        
    command_map = {
        "new": cli.bb_create_repo,
        "delete": cli.bb_delete_repo,
        "edit": cli.bb_edit_repo
    }

    for command, function in command_map.items():
        if getattr(args, command):
            if command == "new":
                # Extract arguments for new command (considering optional description)
                # If the command is 'new', the arguments are treated as a list
                # The first element is the repository name and the second, if present, is the description
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
