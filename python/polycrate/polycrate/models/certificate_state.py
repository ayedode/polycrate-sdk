from typing import Literal

CertificateState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CERTIFICATE_STATE_VALUES: set[CertificateState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_certificate_state(value: str) -> CertificateState:
    if value in CERTIFICATE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_STATE_VALUES!r}")
