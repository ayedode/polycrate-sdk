from typing import Literal

CertificateListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CERTIFICATE_LIST_STATE_VALUES: set[CertificateListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_certificate_list_state(value: str) -> CertificateListState:
    if value in CERTIFICATE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_LIST_STATE_VALUES!r}")
