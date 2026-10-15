from typing import Literal

CredentialLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CREDENTIAL_LAST_STATE_VALUES: set[CredentialLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_credential_last_state(value: str) -> CredentialLastState:
    if value in CREDENTIAL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_LAST_STATE_VALUES!r}")
