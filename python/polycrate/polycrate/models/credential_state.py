from typing import Literal

CredentialState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CREDENTIAL_STATE_VALUES: set[CredentialState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_credential_state(value: str) -> CredentialState:
    if value in CREDENTIAL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_STATE_VALUES!r}")
