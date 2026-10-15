from typing import Literal

OrganizationState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ORGANIZATION_STATE_VALUES: set[OrganizationState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_organization_state(value: str) -> OrganizationState:
    if value in ORGANIZATION_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_STATE_VALUES!r}")
