# Development Guide for mcp-cldkctl

> **Security Note:** Never commit your real tokens or secrets to the repository. All authentication is handled via environment variables or user input. Example tokens in this documentation are placeholders only.

## Setting Up for Development

1. Clone the repository:
   ```sh
   git clone https://github.com/cloudeka/mcp-cldkctl.git
   cd mcp-cldkctl
   ```
2. Install dependencies:
   ```sh
   pip install -e .[dev]
   ```

## Code Style
- Follows Black and isort formatting.
- Type checking with mypy.


## Contributing
- Please open issues or pull requests for any changes or suggestions. 

---

**Before pushing to GitHub, always check your .gitignore to ensure no secrets, cache files, or local config are tracked.** 