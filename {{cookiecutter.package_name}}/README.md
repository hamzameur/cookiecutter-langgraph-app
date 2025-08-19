# {{ cookiecutter.package_name }}

## Quick-start

1. Make sure the `.env` file is created based on the provided `.example.env` sample file and updated with the right variables. 
2. Run the following command :

```sh
docker-compose up --build
```

Visit https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:{{cookiecutter.langgraph_app_port}} to play with the agent.

## Dev

### Prerequisites

This project uses [uv](https://docs.astral.sh/uv/#installation) to manage the python project. Make sure you have it installed

### Installing the virtual environment

Simply run :

```sh
uv sync
```

If you want ti use frozen dependencies, run :

```sh
uv sync --frozen
```
