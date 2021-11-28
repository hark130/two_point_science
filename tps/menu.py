"""Defines Two Point Science package modular menu functionality.

Defines a get_choice() API and Menu namedtuple to reduce redundancy.

    Typical usage example:

    from tps.tph_menu import get_choice, Menu
    choice_menu = Menu('CHOOSE!', {1: 'like', 2: 'love', 3: 'LOVE'})
    feeling = get_choice(choice_menu, choice_type=int)
    print(f'You {feeling} this science!')
"""

# Standard Imports
from collections import namedtuple

# Third Party Imports
from typing import Any
import graphviz

# Local Imports
from tps.misc import clear_screen as clr_screen, print_danger_table
from tps.tph_hospital import TPHHospital

Menu = namedtuple('Menu', 'name dictionary')


def danger_menu(hospital: TPHHospital) -> None:
    """Execute the Two Point Science danger table menu.

    This menu allows the user to print a table with hospital's illnesses and their treatment rooms
    associated with their difficulty, chance of death, and rate of health decline.  The numeric
    factors are presented as an aggregate column.  The menu also allows the user to sort the table
    by column as well as let the user sort the table in ascending or descending order.

    Args:
        hospital: TPHHospital object. (see: tph_hospital module)

    Raises:
        TypeError: Bad data type passed in.
        RuntimeError: Mismatch in internal sort column or sort order variables
    """
    # LOCAL VARIABLES
    sort_col = 6          # Column to sort the Illness Danger Table
    agg_strat = 2         # Aggregate strategy choice
    sort_dir = 'desc'     # Print current sort direction in the menu title
    sort_desc = True      # Converts user sort order choice to print_edge_table() kwarg
    user_input = 0        # User selection
    clear_screen = True   # Clear the screen before printing a menu
    max_chances = 3       # Maximum number of invalid inputs tolerated
    curr_err = ''         # Temp variable which controls error handling
    # Dictionary of sort options
    sort_dict = {1: 'Illness', 2: 'Treatment Room', 3: 'Difficulty', 4: 'Death Chance',
                 5: 'Health Decline', 6: 'Aggregate'}
    # Dictionary of aggregate strategy options
    aggregate_dict = {1: 'Product', 2: 'Average', 3: 'Product & Average Mean'}
    # Template error message for invalid selections
    err_template = '\n*** ERROR: {}***\n'
    # Template menu title
    menu_title_template = \
        'ILLNESS DANGER MENU\nSorted by {} in a {} order\nAggregate strategy: {}\n'
    # Menu dictionary
    menu_dict = {1: 'Print illness danger table', 2: 'Change Column', 3: 'Toggle Sort',
                 4: 'Change aggregate strategy', 999: 'Return to main menu'}

    # INPUT VALIDATION
    # hospital
    if not isinstance(hospital, TPHHospital):
        raise TypeError(f'The hospital can not be of type {type(hospital)}')

    # EDGE MENU
    while True:
        user_input = get_choice(
            tph_menu=Menu(menu_title_template.format(sort_dict[sort_col].lower(), sort_dir,
                                                     aggregate_dict[agg_strat]), menu_dict),
            clear_screen=clear_screen, choice_type=int, max_chances=max_chances,
            return_choice=True)
        clear_screen = True  # Reset temp variable

        # 1. Print Table
        if user_input == 1:
            print_danger_table(hospital, sort_by_col=sort_col, agg_strat=agg_strat,
                               sort_desc=sort_desc)
            clear_screen = False  # Let them see the table
        # 2. Change Column
        elif user_input == 2:
            sort_col = get_choice(tph_menu=Menu('CHANGE SORT COLUMN', sort_dict),
                                  clear_screen=False, choice_type=int, max_chances=max_chances,
                                  return_choice=True)
        # 3. Toggle Sort
        elif user_input == 3:
            if sort_dir == 'desc' and sort_desc:
                sort_dir = 'asc'
                sort_desc = False
            elif sort_dir == 'asc' and not sort_desc:
                sort_dir = 'desc'
                sort_desc = True
            else:
                raise RuntimeError('Mismatch in danger menu sort direction toggle settings')
        # 4. Change Aggregate Strategy
        elif user_input == 4:
            agg_strat = get_choice(tph_menu=Menu('CHANGE AGGREGATE STRATEGY', aggregate_dict),
                                   clear_screen=False, choice_type=int, max_chances=max_chances,
                                   return_choice=True)
        # 999. Exit
        elif user_input == 999:
            return
        else:
            curr_err = err_template.format('INVALID SELECTION')

        # Is there an error?
        if curr_err:
            print(curr_err)
            max_chances = max_chances - 1
            if max_chances < 1:
                print(err_template.format('TOO MANY INVALID SELECTIONS'))
                return
            clear_screen = False  # Let them see the mistake they've made
            curr_err = ''


def get_choice(tph_menu: Menu, clear_screen: bool = True, choice_type: type = str,
               max_chances: int = 3, return_choice: bool = False) -> Any:
    """Prints a menu, reads/converts user input, returns choice.

    Prints the name of the tph_menu and then a list of selections.  Reads user input, converts
    the input to choice_type (default: str).  Reads the choice from the tph_menu and returns it.

    Args:
        tph_menu: Named tuple, defined in the module, containing the menu name and dictionary
            of user choices.
        clear_screen: Optional; Clears the screen, in operating system-appropriate ways, before
            printing anything from tph_menu.
        choice_type: Optional; The data type to convert the user's selection into.  PRO TIP: This
            should be the same data type as the keys in your tph_menu.dictionary.
        max_chances: Optional; Maximum number of inputs to accept from the user before it gives up.
        return_choice: Optional; If true, return the choice instead of the tph_menu value.

    Returns:
        A value from tph_menu.dictionary that matches user input.

    Raises:
        TypeError: An argument was the wrong data type
        RuntimeError: User's invalid selections exceeded max_chances
    """
    # LOCAL VARIABLES
    user_choice = None  # User input
    num_attempts = 0    # Number of attempts at taking user input
    ret_val = None      # Value associated with the user choice

    # INPUT VALIDATION
    _validate_get_choice(tph_menu=tph_menu, clear_screen=clear_screen, choice_type=choice_type,
                         max_chances=max_chances, return_choice=return_choice)

    # DO IT
    # Clear Screen
    if clear_screen:
        clr_screen()
    # Print Menu
    print('\n' + tph_menu.name)
    for option, description in tph_menu.dictionary.items():
        print(f'{option}: {description}')
    while True:
        # Take User Input
        user_choice = read_user_input(choice_type=choice_type)
        num_attempts += 1
        # Validate User Input
        try:
            if return_choice:
                if user_choice in tph_menu.dictionary.keys():
                    ret_val = user_choice
                else:
                    raise KeyError("User's choice of {user_choice} is not valid")
            else:
                ret_val = tph_menu.dictionary[user_choice]
        except KeyError:
            if num_attempts >= max_chances:
                raise RuntimeError('User failures exceeded maximum chances')
            print(f'{user_choice} is an invalid selection.  Try again.')
        else:
            return ret_val


def read_user_input(choice_type: type) -> Any:
    """Read user input and convert it to choice_type.

    Read input from the user and convert it to a given data type.

    Args:
        choice_type: A data type, or typing.Any, to convert the user input to.

    Returns:
        User input converted to choice_type.  Any will be converted to a str.

    Raises:
        TypeError: choice_type is not a valid data type
        RuntimeError: User input can not be converted to choice_type
    """
    # LOCAL VARIABLES
    user_input = None   # User input
    user_choice = None  # User input converted to type choice_type

    # INPUT VALIDATION
    # choice_type
    if not isinstance(choice_type, type):
        raise TypeError(f'The choice_type argument can not be of type {type(choice_type)}')

    # GET IT
    print('Enter a selection:')
    user_input = input()

    # CONVERT IT
    try:
        user_choice = choice_type(user_input)
    except ValueError:
        raise RuntimeError(f'Unable to convert user input "{user_input}" to {choice_type}')

    # DONE
    return user_choice


def _check_for_error(curr_err: str, max_chances: int) -> (int, bool):
    """Internal validation functionality for callers implementing a user menu.

    Extricates duplicate code for internal modules implementing user menus.  If an error is
    detected then max_chances is decremented, the error is printed, and clear_screen is returned
    as False (so the user can read the printed error).

    Args:
        curr_err: A string which may or may not contain an error message.  Any content will be
            treated as an error.
        max_chances: Maximum number of invalid inputs tolerated.  Decremented for the return
            value if an error is detected in curr_err.

    Returns:
        A tuple containing max_chances and a "clear_screen" boolean.  The max_chances value is
            decremented if an error is detected.

    Raises:
        RuntimeWarning: If max_chances is decremented below 0.
    """
    # LOCAL VARIABLES
    new_chances = max_chances  # Adjusted number of chances to return
    clear_screen = True        # Caller can clear the screen because there's no error

    # INPUT VALIDATION
    if isinstance(curr_err, str):
        if curr_err:
            new_chances = new_chances - 1
            if new_chances < 1:
                raise RuntimeWarning('TOO MANY INVALID SELECTIONS')
            print(curr_err)
            clear_screen = False

    # DONE
    return tuple((new_chances, clear_screen))


def _validate_get_choice(tph_menu: Menu, clear_screen: bool, choice_type: type, max_chances: int,
                         return_choice: bool) -> None:
    """Validate input on behalf of get_choice()."""
    # INPUT VALIDATION
    # tph_menu
    if not isinstance(tph_menu, Menu):
        raise TypeError(f'The tph_menu must of type Menu instead of {type(tph_menu)}')
    if not isinstance(tph_menu.name, str):
        raise TypeError(f'The tph_menu must of type str instead of {type(tph_menu.name)}')
    if not isinstance(tph_menu.dictionary, dict):
        raise TypeError(f'The tph_menu must of type dict instead of {type(tph_menu.dictionary)}')
    if not tph_menu.dictionary:
        raise ValueError('The tph_menu can not be empty')
    # clear_screen
    if not isinstance(clear_screen, bool):
        raise TypeError('The clear_screen argument must of type bool instead of '
                        f'{type(clear_screen)}')
    # choice_type
    if not isinstance(choice_type, type):
        raise TypeError(f'The choice_type argument can not be of type {type(choice_type)}')
    # max_chances
    if not isinstance(max_chances, int):
        raise TypeError(f'The max_chances argument can not be of type {type(max_chances)}')
    if max_chances < 1:
        raise ValueError(f'The max_chances value ({max_chances}) must be greater than zero')
    # return_choice
    if not isinstance(return_choice, bool):
        raise TypeError('The return_choice argument must of type bool instead of '
                        f'{type(return_choice)}')
