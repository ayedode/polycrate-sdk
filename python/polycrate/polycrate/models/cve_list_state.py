from typing import Literal

CVEListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CVE_LIST_STATE_VALUES: set[CVEListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_cve_list_state(value: str) -> CVEListState:
    if value in CVE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_LIST_STATE_VALUES!r}")
