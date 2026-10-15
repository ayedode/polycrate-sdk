from typing import Literal

CVEState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CVE_STATE_VALUES: set[CVEState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_cve_state(value: str) -> CVEState:
    if value in CVE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_STATE_VALUES!r}")
