from typing import Literal

DomainPublicDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DOMAIN_PUBLIC_DETAIL_STATE_VALUES: set[DomainPublicDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_domain_public_detail_state(value: str) -> DomainPublicDetailState:
    if value in DOMAIN_PUBLIC_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_PUBLIC_DETAIL_STATE_VALUES!r}")
