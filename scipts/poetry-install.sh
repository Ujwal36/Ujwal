#!/bin/bash

# exit if any of these error
set -e

# Grab the auth token for CodeArtifact and configure Poetry
export CODEARTIFACT_TOKEN=$(aws codeartifact get-authorization-token --domain equipmentshare --domain-owner 696398453447 --query authorizationToken --output text)

echo "Configuring Poetry..."
poetry config virtualenvs.in-project true
poetry config http-basic.codeartifact-dev aws $CODEARTIFACT_TOKEN
poetry config http-basic.codeartifact-prod aws $CODEARTIFACT_TOKEN

echo "Creating virtual environment & installing dependencies..."
poetry install
