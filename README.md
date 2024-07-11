# PyBucket 

## ctrl+s :v:

Welcome to PyBucket, a CLI (Command Line Interface) developed in Python with the purpose of simplifying interactions with Bitbucket directly from the command line. Currently, PyBucket offers basic functionalities to create, edit, and delete repositories on Bitbucket. This project is under constant development, with plans to expand its features in the future.


## Requirements

+ [python-dotenv](https://github.com/theskumar/python-dotenv)
+ [requests](https://github.com/psf/requests)

    > Note: You'll need to create an app password in your BitBucket settings to grant PyBucket access to your repositories.
    >
    > https://support.atlassian.com/bitbucket-cloud/docs/create-an-app-password/


## Usage

You may want to activate the virtual environment before running the pip install or python commands.

```bash
pip install -r requirements.txt
```

```bash
python app/main.py -h
```

```bash
usage: cli.py [-h] [-n NEW [NEW ...]] [-d DELETE [DELETE ...]] [-e EDIT [EDIT ...]] --workspace WORKSPACE [--project PROJECT] [--public]

PyBucket - A tiny BitBucket CLI.

optional arguments:
  -h, --help            show this help message and exit
  -n NEW [NEW ...], --new NEW [NEW ...]
                        Create a new repository on BitBucket.
                        Usage: -n REPO_NAME [DESCRIPTION] --project <project_id> --workspace <workspace_name>
  -d DELETE [DELETE ...], --delete DELETE [DELETE ...]
                        Deletes a repository on BitBucket.
                        Usage: -d REPO_NAME --workspace <workspace_name>
  -e EDIT [EDIT ...], --edit EDIT [EDIT ...]
                        Edit a repository on BitBucket.
                        Usage: -e REPO_NAME [--description NEW_DESCRIPTION] [--public]
  --workspace WORKSPACE
                        Bitbucket Workspace Name
  --project PROJECT     Bitbucket Project Id
  --public              Specify if the repository should be public

```

---

Thank you for considering **PyBucket** for your needs. While it may be a modest tool compared to others, I hope it proves useful in simplifying your interactions with Bitbucket. If you have any feedback or suggestions, don't hesitate to reach out. Nice coding!

<br />
<br />
<div align="center">
	<a href="https://bitbucket.org/rmottalabs/"><img alt="Static Badge" src="https://img.shields.io/badge/-Bitbucket?style=social&logo=bitbucket&logoSize=auto&label=Bitbucket&link=https%3A%2F%2Fbitbucket.org%2Frmottalabs%2Fworkspace%2Foverview%2F"></a>
	<a href="https://gitlab.com/rmottanet"><img alt="Static Badge" src="https://img.shields.io/badge/-Gitlab?style=social&logo=gitlab&logoSize=auto&label=Gitlab&link=https%3A%2F%2Fgitlab.com%2Frmottanet"></a>
	<a href="https://github.com/rmottanet"><img alt="Static Badge" src="https://img.shields.io/badge/-Github?style=social&logo=github&logoSize=auto&label=Github&link=https%3A%2F%2Fgithub.com%2Frmottanet"></a>
	<a href="https://hub.docker.com/"><img alt="Static Badge" src="https://img.shields.io/badge/-DockerHub?style=social&logo=docker&logoSize=auto&label=DockerHub&link=https%3A%2F%2Fhub.docker.com%2Fu%2Frmottanet"></a>
</div>
