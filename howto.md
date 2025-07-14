# How To Use mcp-cldkctl

> **Security Note:** Never commit your real tokens or secrets to the repository. All authentication is handled via environment variables or user input. Example tokens in this documentation are placeholders only.

## Installation

```sh
pip install mcp-cldkctl
# or
uvx mcp-cldkctl
```

## Authentication

Set your token and base URL:
```sh
export CLDKCTL_TOKEN="your_token_here"
export CLDKCTL_BASE_URL="https://ai.cloudeka.id"
```

## Basic Usage

List projects:
```sh
mcp-cldkctl project list
```

Check balance:
```sh
mcp-cldkctl balance detail --project-id <your_project_id>
```

Switch environment:
```sh
mcp-cldkctl switch-environment --env staging
```

## More Information
- See the README.md for full documentation.
- For development, see development.md. 

---

**Before pushing to GitHub, always check your .gitignore to ensure no secrets, cache files, or local config are tracked.**

---

## Deploying to PyPI

To publish this package to PyPI:

1. Build the package:
   ```sh
   python -m build
   ```
2. Upload to PyPI:
   ```sh
   python -m twine upload dist/*
   ```

Make sure you have a valid PyPI account and your credentials are set up (see the [official Twine documentation](https://twine.readthedocs.io/en/stable/) for details). 