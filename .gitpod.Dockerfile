FROM gitpod/workspace-python-3.8:latest

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.4.2 python3 -

ENV AWS_DEFAULT_REGION=us-west-2

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscli.zip" \
  && unzip awscli.zip \
  && sudo ./aws/install --update \
  && rm awscli.zip
