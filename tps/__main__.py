"""Executes the Two Point Science package.

Executes main() from the tph_main module.

    Typical usage example:

    python3 -m tps
"""

# Standard
import sys
# Third Party
# Local
from tps.tph_main import main

if __name__ == '__main__':
    sys.exit(main())
