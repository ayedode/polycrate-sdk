from typing import Literal

CertificateLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CERTIFICATE_LAST_STATE_VALUES: set[CertificateLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_certificate_last_state(value: str) -> CertificateLastState:
    if value in CERTIFICATE_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_LAST_STATE_VALUES!r}")
