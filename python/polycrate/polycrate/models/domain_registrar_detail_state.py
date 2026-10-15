from typing import Literal

DomainRegistrarDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DOMAIN_REGISTRAR_DETAIL_STATE_VALUES: set[DomainRegistrarDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_domain_registrar_detail_state(value: str) -> DomainRegistrarDetailState:
    if value in DOMAIN_REGISTRAR_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_STATE_VALUES!r}")
