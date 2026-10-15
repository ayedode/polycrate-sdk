from typing import Literal

CredentialListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CREDENTIAL_LIST_STATE_VALUES: set[CredentialListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_credential_list_state(value: str) -> CredentialListState:
    if value in CREDENTIAL_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_LIST_STATE_VALUES!r}")
