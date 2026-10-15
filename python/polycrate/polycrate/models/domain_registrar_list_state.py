from typing import Literal

DomainRegistrarListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DOMAIN_REGISTRAR_LIST_STATE_VALUES: set[DomainRegistrarListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_domain_registrar_list_state(value: str) -> DomainRegistrarListState:
    if value in DOMAIN_REGISTRAR_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_LIST_STATE_VALUES!r}")
