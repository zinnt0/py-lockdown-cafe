from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> None:

    masks_to_buy = 0

    for friend in friends:
        if not friend.get("wearing_a_mask", False):
            masks_to_buy += 1

        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            pass

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
