"""Defines the TPHIllness class.

TPHIllness class validates and parses one illness from the game Two Point Hospital.

    Typical usage example:

    illness = TPHIllness('Clamp')
    print(f'Illness: {illness.get_name()}')  # Clamp
    diag_rooms = illness.get_diag()          # ["GP's Office"]
    treat_rooms = illness.get_treat()        # 'Pharmacy'
"""

# Standard
from typing import List

# Third Party

# Local
from tps.tph_constants import (TPH_DIAGNOSTIC_LIST, TPH_ILLNESS_DICT, TPH_ILLNESS_LIST,
                               TPH_NAME_ROOM_GP, TPH_TREATMENT_LIST)


class TPHIllness:
    """Defines one Two Point Hospital illness."""

    # CLASS ATTRIBUTES
    illness_dict = TPH_ILLNESS_DICT
    illness_list = TPH_ILLNESS_LIST
    treat_room_list = TPH_TREATMENT_LIST
    diag_room_list = TPH_DIAGNOSTIC_LIST

    def __init__(self, illness_name: str) -> None:
        """TPHIllness class ctor.

        Creates an object for illness_name

        Raises:
            TypeError: illness_name is not a string.
            ValueError: Invalid illness_name (e.g., empty, not found).
            NotImplementedError: Malformed/Incomplete internal data.
        """
        # INPUT VALIDATION
        if not isinstance(illness_name, str):
            raise TypeError(f'Illness name must be of type str instead of {type(illness_name)}')
        if not illness_name:
            raise ValueError('Illness name can not be empty')
        if illness_name not in self.illness_list:
            raise ValueError('Unknown illness name')

        # INSTANCE ATTRIBUTES
        self._illness_name = illness_name  # Name of the illness
        try:
            self._illness_diag = self.illness_dict[self._illness_name].diagnostic  # Diag rooms
            self._illness_treat = self.illness_dict[self._illness_name].treatment  # Treatment room
        except (AttributeError, KeyError):
            raise NotImplementedError(f'Malformed dictionary entry for {self._illness_name}')

    def get_diag(self) -> List[str]:
        """Retrieves the list of diagnostic rooms for the illness.

        Prepends GP's Room to the list if it doesn't already exist.
        """
        # LOCAL VARIABLES
        illness_diag = None  # List of diagnostic rooms

        # INTERNAL VALIDATION
        if isinstance(self._illness_diag, list):
            illness_diag = self._illness_diag
        elif isinstance(self._illness_diag, str):
            illness_diag = [self._illness_diag]
        if illness_diag:
            # Prepend GP's Room
            if TPH_NAME_ROOM_GP not in illness_diag:
                illness_diag = [TPH_NAME_ROOM_GP] + illness_diag
            # Validate Contents
            for diag_room in illness_diag:
                if not isinstance(diag_room, str):
                    illness_diag = None
                    break
                if diag_room not in self.diag_room_list:
                    illness_diag = None
                    break

        # DONE
        return illness_diag

    def get_name(self) -> str:
        """Return the name of the illness."""
        return self._illness_name

    def get_treat(self) -> str:
        """Retrieves the treatment room for the illness."""
        # LOCAL VARIABLES
        illness_treat = None  # Treatment room

        # INTERNAL VALIDATION
        # print(f'ILLNESS TREATMENT ROOM: {self._illness_treat}')  # DEBUGGING
        if isinstance(self._illness_treat, str) and self._illness_treat in self.treat_room_list:
            illness_treat = self._illness_treat

        # DONE
        return illness_treat
