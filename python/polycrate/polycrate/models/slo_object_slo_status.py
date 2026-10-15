from typing import Literal

SloObjectSloStatus = Literal["at_risk", "breach", "ok"]

SLO_OBJECT_SLO_STATUS_VALUES: set[SloObjectSloStatus] = {
    "at_risk",
    "breach",
    "ok",
}


def check_slo_object_slo_status(value: str) -> SloObjectSloStatus:
    if value in SLO_OBJECT_SLO_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SLO_OBJECT_SLO_STATUS_VALUES!r}")
