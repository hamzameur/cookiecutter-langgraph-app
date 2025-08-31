# Langgraph App Template

## Overview

This repository proposes a boilerplate to create langgraph projects in few clicks.

With this template you have all necessary tools to build and dockerize an agentic AI Langgraph application.

## Prerequisites
You MUST have the following tools installed : 
1. [cookiecutter](https://github.com/cookiecutter/cookiecutter?tab=readme-ov-file#installation) 
2. [uv](https://docs.astral.sh/uv/#installation) to manage python versions and virtual environments efficiently
3. [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/)

## Quick Start

1. run the following command to initiate your `Langgrapĥ` project:

    ```sh
    cookicutter <url-of-this-repository>
    ```

2. when prompted, enter the following variables:
   - `package_name` : name of the python package that will contain your project
   - `langgraph_app_port` :  port on which your langgraph app will be served (default is 2024)

3. cd the newly created project:

    ```sh
    cd <your-package-name>
    ```

4. DEV - start app using `docker-compose`:

    ```sh
    docker-compose up --build
    ```
    Visit "https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024" (replace **with your own port**) to play with the sample agent.

5. DEV - install python project dependencies using `uv`:

    ```sh
    uv sync
    ```

6. (optional) create git repository and push your code.
   - initialize repository :
    ```sh
    git init
    ```
   - add files:
    ```sh
    git add .
    ```
   - commit files:
    ```sh
    git commit -m "init"
    ```
   - set project url:
    ```sh
    git remote add origin <url-of-your-new-project>
    ```
   - push your code:
    ```sh
    git push origin main
    ```
