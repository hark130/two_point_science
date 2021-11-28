"""Defines the TPHIllness class.

TPHIllness class validates and parses one illness from the game Two Point Hospital.

    Typical usage example:

    illness = TPHIllness('Clamp')
    print(f'Illness: {illness.get_name()}')  # Clamp
    diag_rooms = illness.get_diag()          # ["GP's Office"]
    treat_rooms = illness.get_treat()        # 'Pharmacy'
"""

# Standard
from typing import Any, List

# Third Party

# Local
from tps.tph_constants import (MISSING_DATA, TPH_DIAGNOSTIC_LIST, TPH_ILLNESS_DICT,
                               TPH_ILLNESS_LIST, TPH_NAME_ROOM_GP, TPH_TREATMENT_LIST)


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
            # Diag rooms
            self._illness_diag = self.illness_dict[self._illness_name].diagnostic
            # Treatment room
            self._illness_treat = self.illness_dict[self._illness_name].treatment
            # Illness difficulty
            self._illness_difficulty = self.illness_dict[self._illness_name].difficulty
            # Chance of death
            self._illness_death = self.illness_dict[self._illness_name].death
            # Health loss severity
            self._illness_decline = self.illness_dict[self._illness_name].decline
        except (AttributeError, KeyError):
            raise NotImplementedError(f'Malformed dictionary entry for {self._illness_name}')
        self._validate_attributes()

    def get_aggregate_value(self, strategy: int = 2) -> Any:
        """Return the illness danger aggregate value.

        Aggregate value is determined by strategy.  The source values are difficulty,
        chance of death, and health decline rate.  Any values of MISSING_DATA are calculated as 1.

        Args:
            strategy: Optional; If 1, return the product of the source values.  If 2, return
                the average of the source values.  If 3, return the average of strategy 1 and 2.

        Raises:
            TypeError: Bad data type
            ValueError: Invalid strategy value
        """
        # LOCAL VARIABLES
        # Aggregate source values
        val_list = [self.get_difficulty_value(), self.get_death_value(), self.get_decline_value()]
        product = 0    # Strategy 1
        average = 0    # Strategy 2
        aggregate = 0  # Calculated aggregate value

        # INPUT VALIDATION
        if not isinstance(strategy, int):
            raise TypeError(f'The strategy argument can not be of type {type(strategy)}')
        if strategy not in (1, 2, 3):
            raise ValueError(f'The strategy selection of {strategy} is invalid')

        # GET IT
        # Validate aggregate source values
        for index, value in enumerate(val_list):
            if value == MISSING_DATA:
                val_list[index] = 1  # Missing data is a mathematical pass
        # Calculate values
        product = val_list[0] * val_list[1] * val_list[2]
        average = (val_list[0] + val_list[1] + val_list[2]) / 3
        if strategy == 1:
            aggregate = product
        elif strategy == 2:
            aggregate = average
        elif strategy == 3:
            aggregate = (product + average) / 2
        else:
            raise NotImplementedError(f'Strategy value {strategy} passed validation?!')

        # DONE
        return aggregate

    def get_aggregate_str(self, strategy: int = 2) -> str:
        """Convert aggregate value to a percent string.

        Aggregate value is determined by strategy.  The source values are difficulty,
        chance of death, and health decline rate.  Any values of MISSING_DATA are calculated as 1.

        Args:
            strategy: Optional; If 1, return the product of the source values.  If 2, return
                the average of the source values.  If 3, return the average of strategy 1 and 2.

        Raises:
            TypeError: Bad data type
            ValueError: Invalid strategy value
        """
        # LOCAL VARIABLES
        ag_percent = ''                              # Convert aggregate to a string here
        ag_val = self.get_aggregate_value(strategy)  # Store aggregate value here

        # DO IT
        if ag_val == MISSING_DATA:
            ag_percent = 'MISSING DATA'  # This should never happen
        else:
            ag_percent = str(int(ag_val * 100)) + '%'

        # DONE
        return ag_percent

    def get_death_value(self) -> Any:
        """Return the chance of death."""
        return self._illness_death

    def get_death_str(self) -> str:
        """Convert death chance to a percent string."""
        # LOCAL VARIABLES
        death_percent = ''                 # Convert difficulty to a string here
        death_val = self.get_death_value()  # Store difficulty value here

        # DO IT
        if death_val == MISSING_DATA:
            death_percent = 'MISSING DATA'
        else:
            death_percent = str(int(death_val * 100)) + '%'

        # DONE
        return death_percent

    def get_decline_value(self) -> Any:
        """Return the health loss severity."""
        return self._illness_decline

    def get_decline_str(self) -> str:
        """Convert health loss severity to a percent string."""
        # LOCAL VARIABLES
        decline_percent = ''                 # Convert difficulty to a string here
        decline_val = self.get_decline_value()  # Store difficulty value here

        # DO IT
        if decline_val == MISSING_DATA:
            decline_percent = 'MISSING DATA'
        else:
            decline_percent = str(int(decline_val * 100)) + '%'

        # DONE
        return decline_percent

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

    def get_difficulty_value(self) -> Any:
        """Return the difficulty."""
        return self._illness_difficulty

    def get_difficulty_str(self) -> str:
        """Convert difficulty to a percent string."""
        # LOCAL VARIABLES
        diff_percent = ''                       # Convert difficulty to a string here
        diff_val = self.get_difficulty_value()  # Store difficulty value here

        # DO IT
        if diff_val == MISSING_DATA:
            diff_percent = 'MISSING DATA'
        else:
            diff_percent = str(int(diff_val * 100)) + '%'

        # DONE
        return diff_percent

    def get_name(self) -> str:
        """Return the name of the illness."""
        return self._illness_name

    def get_treat(self) -> str:
        """Retrieves the treatment room for the illness."""
        # LOCAL VARIABLES
        illness_treat = None  # Treatment room

        # INTERNAL VALIDATION
        if isinstance(self._illness_treat, str) and self._illness_treat in self.treat_room_list:
            illness_treat = self._illness_treat

        # DONE
        return illness_treat

    def _validate_attributes(self) -> None:
        # self._illness_diag
        # self._illness_treat
        _validate_num(self._illness_difficulty)
        _validate_num(self._illness_death)
        _validate_num(self._illness_decline)


def _validate_num(num: Any) -> None:
    """Validate number value as percentage."""
    if num == MISSING_DATA:
        pass  # Undefined data.  Let it ride.
    elif not isinstance(num, int) and not isinstance(num, float):
        raise TypeError(f'Value {num}, of type {type(num)}, is not a valid number type')
    elif num < 0:
        raise ValueError(f'Value {num} is not valid as a percentage')
