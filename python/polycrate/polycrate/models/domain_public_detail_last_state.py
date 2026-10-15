from typing import Literal

DomainPublicDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DOMAIN_PUBLIC_DETAIL_LAST_STATE_VALUES: set[DomainPublicDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_domain_public_detail_last_state(value: str) -> DomainPublicDetailLastState:
    if value in DOMAIN_PUBLIC_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_PUBLIC_DETAIL_LAST_STATE_VALUES!r}")
