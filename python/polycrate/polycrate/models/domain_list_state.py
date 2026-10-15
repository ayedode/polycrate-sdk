from typing import Literal

DomainListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DOMAIN_LIST_STATE_VALUES: set[DomainListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_domain_list_state(value: str) -> DomainListState:
    if value in DOMAIN_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_LIST_STATE_VALUES!r}")
