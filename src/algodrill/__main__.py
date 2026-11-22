"""Allow ``python -m algodrill`` to run the CLI."""

from algodrill.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
