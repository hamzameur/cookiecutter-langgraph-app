# Langgraph app template

## Usage

This repository proposes a boilerplate to create langgraph projects in few clicks.

## Prerequisites
You must have the following tools installed : 
1. [cookiecutter](https://github.com/cookiecutter/cookiecutter?tab=readme-ov-file#installation) 
2. python >= 3.12.1 : use [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) to manage python versions efficiently
3. [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/)
4. [poetry](https://python-poetry.org/docs/#installation)

## Quick-start

1. run the following command to initiate your langgrapĥ project

```sh
cookicutter <url-of-this-repository>
```

2. when prompted, enter the following variables :
- `package_name` : name of the python package that will contain your project
- `langgraph_app_port` :  port on which your langgraph app will be served (default is 2024)

3. enter the newly created project

```sh
cd <your-package-name>
```

4. DEV: start app

```sh
docker-compose up --build
```
Visit https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:<your-port> to play with the sample agent.

5. DEV: install dependencies

```sh
poetry install
```

7. (optional) create git repository
- initialize repository
```sh
git init
```
- add files
```sh
git add .
```
- commit files
```sh
git commit -m "init"
```
- add remote url
```sh
git remote add origin <url-of-your-new-project>
```
- push your repository
```sh
git push origin main
```
