"""Executes the Two Point Science package.

Executes main() from the tph_main module.

    Typical usage example:

    python3 -m tps
"""

# Standard
import sys

# Third Party

# Local
from tps.main import main
from tps.misc import print_exception

if __name__ == '__main__':
    # LOCAL VARIABLES
    EXIT_VAL = 0  # 0 on success, 1 on error

    # DO IT
    try:
        main()
    except Exception as err:  # pylint:disable=broad-except
        print_exception(err)
        EXIT_VAL = 1

    # DONE
    sys.exit(EXIT_VAL)
