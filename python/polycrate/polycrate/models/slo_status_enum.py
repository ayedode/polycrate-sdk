from typing import Literal

SloStatusEnum = Literal["at_risk", "breach", "ok"]

SLO_STATUS_ENUM_VALUES: set[SloStatusEnum] = {
    "at_risk",
    "breach",
    "ok",
}


def check_slo_status_enum(value: str) -> SloStatusEnum:
    if value in SLO_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SLO_STATUS_ENUM_VALUES!r}")
