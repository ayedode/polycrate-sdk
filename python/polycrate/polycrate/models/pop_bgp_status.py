from typing import Literal

PopBgpStatus = Literal["no", "planned", "unknown", "yes"]

POP_BGP_STATUS_VALUES: set[PopBgpStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_bgp_status(value: str) -> PopBgpStatus:
    if value in POP_BGP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_BGP_STATUS_VALUES!r}")
