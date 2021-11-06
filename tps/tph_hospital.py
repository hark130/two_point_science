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
