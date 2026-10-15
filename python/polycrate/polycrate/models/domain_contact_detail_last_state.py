from typing import Literal

DomainContactDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DOMAIN_CONTACT_DETAIL_LAST_STATE_VALUES: set[DomainContactDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_domain_contact_detail_last_state(value: str) -> DomainContactDetailLastState:
    if value in DOMAIN_CONTACT_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_DETAIL_LAST_STATE_VALUES!r}")
