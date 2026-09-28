"""Application bootstrap script."""

import sys
from atm.controller import ATMController


def main() -> None:
    try:
        controller = ATMController(config_path="config.json")
        controller.run()
    except KeyboardInterrupt:
        print("\n\nOperation aborted by user. Exiting securely...")
        sys.exit(0)
    except FileNotFoundError as err:
        print(f"System configuration error: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()