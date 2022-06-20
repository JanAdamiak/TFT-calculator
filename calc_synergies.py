from lib2to3.pytree import Base
from xmlrpc.client import Boolean
from constants import DEFAULT_SYNERGIES, SYNERGY_TRESHOLDS, CHAMPIONS, DRAGON_CHAMPIONS
from data_types import StringTuple, SynergyCounter


class SynergyCalculator:
    def __init__(self, units: StringTuple, additional_synergies: StringTuple=None) -> None:
        if not units:
            raise BaseException("Can't initiate class with no units.")
        self.units = set(units)
        self.additional_synergies = additional_synergies

        self.validate_units()
        if self.additional_synergies:
            self.validate_additional_synergies()

        self.dragon_unit = self.dragon_present()
        self.synergies = self.get_current_synergies()

    def dragon_present(self) -> Boolean:
        for dragon in DRAGON_CHAMPIONS:
            if dragon in self.units:
                return True
        return False

    def validate_units(self) -> None:
        for unit in self.units:
            if unit not in CHAMPIONS:
                raise BaseException("Unit not recognized")

    def validate_additional_synergies(self) -> None:
        for additional_synergies in self.additional_synergies:
            if additional_synergies not in DEFAULT_SYNERGIES:
                raise BaseException("Synergy not recognized")

    def get_current_synergies(self) -> SynergyCounter:
        synergies = DEFAULT_SYNERGIES
        for unit in self.units:
            for synergy in CHAMPIONS[unit]:
                synergies[synergy] = synergies[synergy] + 1
        return synergies

    def amount_of_synergies(self) -> int:
        counter = 0
        for synergy, value in self.synergies.items():
            if value > 0:
                for count, tresholds in enumerate(tuple(0, *SYNERGY_TRESHOLDS[synergy])):
                    if tresholds > self.synergies[synergy]:
                        count -= 1
                        break
                counter += count
        return counter

    def compute_options(self):
        pass
        # FLOWS:

        # Dragon present:
        # +0
        # 1. Replace dragon
        # 2. Replace unit
        # +1
        # 3. Add unit
        # 4. Replace dragon + add unit
        # 5. Replace unit + add unit
        # +2
        # 6. Add 2 units
        # 7. Replace dragon for 2 units

        # Dragon not present:
        # +0
        # 1. Replace 2 units for dragon
        # 2. Replace unit
        # +1
        # 3. Add unit
        # 4. Replace dragon + add unit
        # 5. Replace unit + add unit
        # +2
        # 6. Add 2 units
        # 7. Replace dragon for 2 units
