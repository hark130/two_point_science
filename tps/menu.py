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

# Local Imports
from tps.tph_misc import clear_screen as clr_screen

Menu = namedtuple('Menu', 'name dictionary')


def get_choice(tph_menu: Menu, clear_screen: bool = True, choice_type: type = str,
               max_chances: int = 3) -> Any:
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

    Returns:
        A value from tph_menu.dictionary that matches user input.

    Raises:
        TypeError: error is not an Exception (or inherited from) type.
    """
    # LOCAL VARIABLES
    user_choice = None  # User input
    num_attempts = 0    # Number of attempts at taking user input
    dict_value = None   # Value associated with the user choice

    # INPUT VALIDATION
    _validate_get_choice(tph_menu=tph_menu, clear_screen=clear_screen, choice_type=choice_type,
                         max_chances=max_chances)

    # DO IT
    # Clear Screen
    if clear_screen:
        clr_screen()
    # Print Menu
    print(tph_menu.name)
    for option, description in tph_menu.dictionary.items():
        print(f'{option}: {description}')
    while True:
        # Take User Input
        user_choice = read_user_input(choice_type=choice_type)
        num_attempts += 1
        # Validate User Input
        try:
            dict_value = tph_menu.dictionary[user_choice]
        except KeyError:
            if num_attempts >= max_chances:
                raise RuntimeError('User failures exceeded maximum chances')
            print(f'{user_choice} is an invalid selection.  Try again.')
        else:
            return dict_value


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


def _validate_get_choice(tph_menu: Menu, clear_screen: bool, choice_type: type, max_chances: int):
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
