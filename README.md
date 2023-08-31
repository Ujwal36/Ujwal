# gitpod-python

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://equipmentshare.gitpod.cloud/#your-gitlab-repo-url)

Template for `python`/`poetry` projects

## Gitpod Onboarding 
- Follow the [onboarding docs](https://www.notion.so/equipmentshare/Gitpod-12de6a3707be456784a08900ec206fe5) to join Gitpod

## Gitpod Files
- Inspect `.gitpod.Dockerfile` for configuration of workspace.  
  - Review ENV VARs 
    - `PYTHON_VERSION`
    - `POETRY_VERSION`
    - `NODE_VERSION`
- Review `.gitpod.yml` for workspace tasks

### Poetry
- `poetry run start` - starter function

### CDK:
NodeJS is included to assit with `cdk` operations:
- `mkdir cdk`
- `cd cdk/`
- `npx aws-cdk init --language typescript`
- `npm run cdk diff`
