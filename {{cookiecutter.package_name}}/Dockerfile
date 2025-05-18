
FROM python:3.12.1-slim as builder

RUN pip install poetry==1.8.1
WORKDIR /{{cookiecutter.package_name}}
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --without-hashes -o requirements.txt

FROM python:3.12.1-slim as final
WORKDIR /{{cookiecutter.package_name}}
COPY --from=builder /{{cookiecutter.package_name}}/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm -f requirements.txt
COPY {{cookiecutter.package_name}}/ {{cookiecutter.package_name}}/
COPY pyproject.toml ./
RUN pip install .
ENV LANGGRAPH_APP_PORT={{cookiecutter.langgraph_app_port}}
EXPOSE $LANGGRAPH_APP_PORT
COPY langgraph.json ./
CMD sh -c "langgraph dev --host 0.0.0.0 --port ${LANGGRAPH_APP_PORT}"