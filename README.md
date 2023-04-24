# gitpod-python

Template for `python`/`poetry` projects


## Gitpod   
### Getting started   
- Review `.gitpod.Dockerfile` for configuration of workspace.   
- Review `.gitpod.yml` for workspace tasks


### Poetry
- `./poetry-install.sh` - script to install from AWS CodeArtifact
- `poetry run start` - starter function

### CDK:
NodeJS is included to assit with `cdk` operations:
- `mkdir cdk`
- `cd cdk/`
- `npx aws-cdk init --language typescript`
- `npm run cdk diff`