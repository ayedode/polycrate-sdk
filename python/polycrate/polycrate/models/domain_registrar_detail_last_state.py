from typing import Literal

DomainRegistrarDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DOMAIN_REGISTRAR_DETAIL_LAST_STATE_VALUES: set[DomainRegistrarDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_domain_registrar_detail_last_state(value: str) -> DomainRegistrarDetailLastState:
    if value in DOMAIN_REGISTRAR_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_LAST_STATE_VALUES!r}")
