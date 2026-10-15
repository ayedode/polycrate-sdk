from typing import Literal

PopRequestBgpStatus = Literal["no", "planned", "unknown", "yes"]

POP_REQUEST_BGP_STATUS_VALUES: set[PopRequestBgpStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_request_bgp_status(value: str) -> PopRequestBgpStatus:
    if value in POP_REQUEST_BGP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_BGP_STATUS_VALUES!r}")
