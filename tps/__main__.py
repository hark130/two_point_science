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
from tps.tph_misc import print_exception

if __name__ == '__main__':
    # LOCAL VARIABLES
    exit_val = 0  # 0 on success, 1 on error

    # DO IT
    try:
        main()
    except Exception as err:
        print_exception(err)
        exit_val = 1

    # DONE
    sys.exit(exit_val)
