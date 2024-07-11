# PyBucket 

## ctrl+s :v:

Salve! Este é o PyBucket, um CLI (Command Line Interface) desenvolvido em Python com o objetivo de simplificar as interações com o Bitbucket diretamente da linha de comando. Atualmente, PyBucket oferece funcionalidades básicas para criar, editar e excluir repositórios no Bitbucket. Este projeto está em constante desenvolvimento, com planos de expansão de suas funcionalidades no futuro.


## Requisitos

+ [python-dotenv](https://github.com/theskumar/python-dotenv)
+ [requests](https://github.com/psf/requests)

    > Nota: Você precisará criar uma senha de aplicativo nas configurações do BitBucket para conceder acesso ao PyBucket aos seus repositórios.
    >
    > https://support.atlassian.com/bitbucket-cloud/docs/create-an-app-password/


## Uso

Você pode querer ativar o ambiente virtual antes de executar os comandos pip install ou python.

```bash
pip install -r requirements.txt
```

```bash
python app/main.py -h
```

```shell

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

Obrigado por considerar o **PyBucket** para suas necessidades. Embora possa ser uma ferramenta modesta em comparação com outras, espero que seja útil para simplificar suas interações com o Bitbucket. Se você tiver algum comentário ou sugestão, não hesite em entrar em contato. Boa codificação!

<br />
<br />
<div align="center">
	<a href="https://bitbucket.org/rmottalabs/"><img alt="Static Badge" src="https://img.shields.io/badge/-Bitbucket?style=social&logo=bitbucket&logoSize=auto&label=Bitbucket&link=https%3A%2F%2Fbitbucket.org%2Frmottalabs%2Fworkspace%2Foverview%2F"></a>
	<a href="https://gitlab.com/rmottanet"><img alt="Static Badge" src="https://img.shields.io/badge/-Gitlab?style=social&logo=gitlab&logoSize=auto&label=Gitlab&link=https%3A%2F%2Fgitlab.com%2Frmottanet"></a>
	<a href="https://github.com/rmottanet"><img alt="Static Badge" src="https://img.shields.io/badge/-Github?style=social&logo=github&logoSize=auto&label=Github&link=https%3A%2F%2Fgithub.com%2Frmottanet"></a>
	<a href="https://hub.docker.com/"><img alt="Static Badge" src="https://img.shields.io/badge/-DockerHub?style=social&logo=docker&logoSize=auto&label=DockerHub&link=https%3A%2F%2Fhub.docker.com%2Fu%2Frmottanet"></a>
</div>
