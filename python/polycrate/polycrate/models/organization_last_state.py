from typing import Literal

OrganizationLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ORGANIZATION_LAST_STATE_VALUES: set[OrganizationLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_organization_last_state(value: str) -> OrganizationLastState:
    if value in ORGANIZATION_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_LAST_STATE_VALUES!r}")
