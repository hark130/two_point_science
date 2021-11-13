"""Defines the TPHHospital class.

TPHHospital class validates and parses one hospital from the game Two Point Hospital.

    Typical usage example:

    site = TPHHospital('Grockle Bay')
    print(f'Hospital: {site.get_name()}')     # Grockle Bay
    for illness in site.get_illness_names():
        print(f'    {illness}')
"""

# Standard
from typing import List

# Third Party

# Local
from tps.tph_constants import TPH_HOSPITAL_DICT, TPH_HOSPITAL_LIST, TPH_ILLNESS_LIST
from tps.tph_illness import TPHIllness


class TPHHospital:
    """Defines one Two Point Hospital."""

    # CLASS ATTRIBUTES
    hospital_dict = TPH_HOSPITAL_DICT
    hospital_list = TPH_HOSPITAL_LIST
    illness_list = TPH_ILLNESS_LIST

    def __init__(self, hospital_name: str) -> None:
        """TPHHospital class ctor.

        Creates an object for hospital_name

        Raises:
            TypeError: hospital_name is not a string.
            ValueError: Invalid hospital_name (e.g., empty, not found).
            NotImplementedError: Malformed/Incomplete internal data
        """
        # INPUT VALIDATION
        if not isinstance(hospital_name, str):
            raise TypeError(f'Hospital name must be of type str instead of {type(hospital_name)}')
        if not hospital_name:
            raise ValueError('Hospital name can not be empty')
        if hospital_name not in self.hospital_list:
            raise ValueError('Unknown hospital name')

        # INSTANCE ATTRIBUTES
        self._hospital_name = hospital_name  # Name of the hospital
        try:
            self._hospital_illnesses = self.hospital_dict[self._hospital_name].illness
        except (AttributeError, KeyError):
            raise NotImplementedError(f'Malformed dictionary entry for {self._hospital_name}')
        self._hospital_illness_objs = None  # Defined, if asked for by caller

    def get_diag_room_list(self, sort_list: bool = True) -> List[str]:
        """Return a list of all diagnostic rooms associated with this hospital."""
        # LOCAL VARIABLES
        ill_obj_list = []  # List of all illness objects for this hospital
        room_list = []     # List of all diagnostic rooms in this hospital

        # INPUT VALIDATION
        if not isinstance(sort_list, bool):
            raise TypeError(f'The sort_list must be of type bool instead of {type(sort_list)}')

        # MAKE LIST
        # Get illness objects
        ill_obj_list = self.get_illness_objects()
        # Build the list
        for ill_obj in ill_obj_list:
            for diag_room in ill_obj.get_diag():
                if diag_room not in room_list:
                    room_list.append(diag_room)
        # Sort?
        if sort_list:
            room_list.sort()

        # DONE
        return room_list

    def get_illness_names(self) -> List[str]:
        """Retrieves the list of illnesses found in this hospital."""
        # LOCAL VARIABLES
        illness_list = None  # List of illnesses

        # INTERNAL VALIDATION
        # print(self._hospital_illnesses)  # DEBUGGING
        if isinstance(self._hospital_illnesses, list):
            illness_list = self._hospital_illnesses
        elif isinstance(self._hospital_illnesses, str):
            illness_list = [self._hospital_illnesses]
        if illness_list:
            for illness in illness_list:
                if not isinstance(illness, str):
                    print(f'INVALID ILLNESS: {illness}')  # DEBUGGING
                    illness_list = None
                    break
                if illness not in self.illness_list:
                    print(f'INVALID ILLNESS: {illness}')  # DEBUGGING
                    illness_list = None
                    break

        # DONE
        return illness_list

    def get_illness_objects(self) -> list:
        """Retrieves TPHIllness objects associated with this hospital.

        Builds object list if necessary.

        Raises:
            TypeError: Illness name is not a string.
            ValueError: Invalid illness name.
            NotImplementedError: Malformed/Incomplete internal data.
        """
        # INTERNAL VALIDATION
        if not self._hospital_illness_objs:
            self._build_illness_objects()

        return self._hospital_illness_objs

    def get_name(self) -> str:
        """Return the name of the hospital."""
        return self._hospital_name

    def get_room_list(self, sort_list: bool = True) -> List[str]:
        """Return a list of all rooms associated with this hospital."""
        # LOCAL VARIABLES
        room_list = []   # List of all rooms in this hospital

        # INPUT VALIDATION
        if not isinstance(sort_list, bool):
            raise TypeError(f'The sort_list must be of type bool instead of {type(sort_list)}')

        # GET LIST
        # Diagnostic Rooms
        room_list = self.get_diag_room_list(sort_list=sort_list)
        # Treament Rooms
        for room in self.get_treat_room_list(sort_list=sort_list):
            if room not in room_list:
                room_list.append(room)
        # Sort?
        if sort_list:
            room_list.sort()

        # DONE
        return room_list

    def get_treat_room_list(self, sort_list: bool = True) -> List[str]:
        """Return a list of all treatment rooms associated with this hospital."""
        # LOCAL VARIABLES
        ill_obj_list = []  # List of all illness objects for this hospital
        room_list = []     # List of all treatment rooms in this hospital

        # INPUT VALIDATION
        if not isinstance(sort_list, bool):
            raise TypeError(f'The sort_list must be of type bool instead of {type(sort_list)}')

        # MAKE LIST
        # Get illness objects
        ill_obj_list = self.get_illness_objects()
        # Build the list
        for ill_obj in ill_obj_list:
            if ill_obj.get_treat() not in room_list:
                room_list.append(ill_obj.get_treat())
        # Sort?
        if sort_list:
            room_list.sort()

        # DONE
        return room_list

    def _build_illness_objects(self) -> None:
        """Builds _hospital_illness_objs list.

        Overwrites whatever may have existed.

        Raises:
            TypeError: Illness name is not a string.
            ValueError: Invalid illness name.
            NotImplementedError: Malformed/Incomplete internal data.
        """
        self._hospital_illness_objs = []  # Reset instance attribute
        # Populate instance attribute
        for illness in self.get_illness_names():
            self._hospital_illness_objs.append(TPHIllness(illness))
