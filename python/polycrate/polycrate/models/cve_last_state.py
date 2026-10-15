from typing import Literal

CVELastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CVE_LAST_STATE_VALUES: set[CVELastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_cve_last_state(value: str) -> CVELastState:
    if value in CVE_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_LAST_STATE_VALUES!r}")
