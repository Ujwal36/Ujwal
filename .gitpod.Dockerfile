FROM gitpod/workspace-full

ENV PYTHON_VERSION=3.11.1
ENV POETRY_VERSION=1.4.2
ENV NODE_VERSION=18.15.0

ENV AWS_DEFAULT_REGION=us-west-2

## PYTHON
RUN pyenv install $PYTHON_VERSION -s \
    && pyenv global $PYTHON_VERSION

## POETRY
RUN curl -sSL https://install.python-poetry.org |  python3 -

## NODE
RUN bash -c 'source $HOME/.nvm/nvm.sh && nvm install $NODE_VERSION \
    && nvm use $NODE_VERSION && nvm alias default $NODE_VERSION'

RUN echo "nvm use default &>/dev/null" >> ~/.bashrc.d/51-nvm-fix

## AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscli.zip" \
  && unzip awscli.zip \
  && sudo ./aws/install --update \
  && rm awscli.zip
