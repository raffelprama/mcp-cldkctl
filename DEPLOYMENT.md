# MCP cldkctl Server Deployment Guide

> **Security Note:** Never commit your real tokens or secrets to the repository. All authentication is handled via environment variables or user input. Example tokens in this documentation are placeholders only.

This guide covers deploying the MCP cldkctl server to PyPI and setting up automated builds.

## Prerequisites

- Python 3.8+ installed
- `uv` package manager installed
- PyPI account with API token
- GitHub repository access

## Local Development Setup

### 1. Install Dependencies

```bash
# Install uv if not already installed
pip install uv

# Sync dependencies
uv sync

# Install in development mode
uv pip install -e .
```

### 3. Code Quality Checks

```bash
# Format code
uv run black .
uv run isort .

# Lint code
uv run flake8 mcp_cldkctl/

# Type checking
uv run mypy mcp_cldkctl/
```

## Building and Publishing

### 1. Update Version

Edit `pyproject.toml` and increment the version:

```toml
[project]
name = "mcp-cldkctl"
version = "0.2.9"  # Increment this
```

### 2. Build Package

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info/

# Build package
uv run python -m build

# Verify build
uv run python -m twine check dist/*
```

### 3. Test Upload (Optional)

```bash
# Upload to TestPyPI first
uv run python -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
uvx mcp-cldkctl --version
```

### 4. Publish to PyPI

```bash
# Upload to PyPI
uv run python -m twine upload dist/*

# Verify installation
uvx mcp-cldkctl --version
```

## Automated Deployment

### GitHub Actions Workflow

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to PyPI

on:
  push:
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install uv
      run: |
        curl -LsSf https://astral.sh/uv/install.sh | sh
        echo "$HOME/.cargo/bin" >> $GITHUB_PATH
    
    - name: Install dependencies
      run: |
        uv sync
    
    - name: Run tests
      run: |
        uv run pytest
    
    - name: Build package
      run: |
        uv run python -m build
    
    - name: Publish to PyPI
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        password: ${{ secrets.PYPI_API_TOKEN }}
```

### Environment Variables

Set these in your GitHub repository secrets:

- `PYPI_API_TOKEN`: Your PyPI API token

## Docker Deployment

### Dockerfile

```dockerfile
FROM python:3.11-slim

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock ./
COPY mcp_cldkctl/ ./mcp_cldkctl/

# Install dependencies
RUN uv sync --frozen

# Expose port (if needed)
EXPOSE 8000

# Run the MCP server
CMD ["uv", "run", "mcp-cldkctl"]
```

### Docker Build and Run

```bash
# Build image
docker build -t mcp-cldkctl .

# Run container
docker run -e CLDKCTL_TOKEN=your_token mcp-cldkctl
```

## Kubernetes Deployment

### Deployment YAML

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mcp-cldkctl
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mcp-cldkctl
  template:
    metadata:
      labels:
        app: mcp-cldkctl
    spec:
      containers:
      - name: mcp-cldkctl
        image: your-registry/mcp-cldkctl:latest
        env:
        - name: CLDKCTL_TOKEN
          valueFrom:
            secretKeyRef:
              name: cldkctl-secret
              key: token
        - name: CLDKCTL_BASE_URL
          value: "https://ai.cloudeka.id"
        ports:
        - containerPort: 8000
```

### Secret for Token

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cldkctl-secret
type: Opaque
data:
  token: <base64-encoded-token>
```

## Environment Configuration

### Production Environment

```bash
# Environment variables
export CLDKCTL_TOKEN="cldkctl_your_production_token"
export CLDKCTL_BASE_URL="https://ai.cloudeka.id"
export CLDKCTL_DEFAULT_PROJECT_ID="your_project_id"

# Run server
uvx mcp-cldkctl
```

### Staging Environment

```bash
# Environment variables
export CLDKCTL_TOKEN="cldkctl_your_staging_token"
export CLDKCTL_BASE_URL="https://staging.ai.cloudeka.id"
export CLDKCTL_DEFAULT_PROJECT_ID="your_staging_project_id"

# Run server
uvx mcp-cldkctl
```

## Monitoring and Logging

### Health Check Endpoint

The MCP server provides a status endpoint:

```python
# Check server status
status()
```

### Logging Configuration

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## Troubleshooting

### Common Issues

1. **Build Failures**
   - Check Python version compatibility
   - Verify all dependencies are listed in `pyproject.toml`
   - Run `uv sync` to update lock file

2. **Import Errors**
   - Ensure package is installed correctly
   - Check `__init__.py` files exist
   - Verify import paths

3. **Authentication Issues**
   - Verify `CLDKCTL_TOKEN` is set correctly
   - Check token format (should start with `cldkctl_`)
   - Test with staging environment

4. **Network Issues**
   - Check firewall settings
   - Verify DNS resolution
   - Test connectivity to Cloudeka endpoints

### Debug Commands

```bash
# Check package installation
uvx mcp-cldkctl --version

# Run with debug output
uvx mcp-cldkctl 2>&1 | tee debug.log
```

## Version Management

### Semantic Versioning

Follow semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, backward compatible

### Release Process

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create git tag: `git tag v0.1.18`
4. Push tag: `git push origin v0.1.18`
5. GitHub Actions will automatically deploy

## Support

For deployment issues:

- Check [GitHub Issues](https://github.com/cloudeka/mcp-cldkctl/issues)
- Review [MCP Documentation](https://modelcontextprotocol.io)
- Contact support@cloudeka.id

---

**Last Updated**: 2024-12-21  
**Version**: 0.2.9 