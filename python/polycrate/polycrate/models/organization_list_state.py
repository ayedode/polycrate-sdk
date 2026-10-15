from typing import Literal

OrganizationListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ORGANIZATION_LIST_STATE_VALUES: set[OrganizationListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_organization_list_state(value: str) -> OrganizationListState:
    if value in ORGANIZATION_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_LIST_STATE_VALUES!r}")
