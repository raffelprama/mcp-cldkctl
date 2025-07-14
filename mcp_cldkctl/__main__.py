"""Entry point for mcp-cldkctl."""
import asyncio
import sys
import traceback
from .server import main


def cli_main():
    """CLI entry point that properly handles the async main function."""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped by user.", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Server error: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    cli_main()