from typing import Literal

IdentityProviderLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

IDENTITY_PROVIDER_LAST_STATE_VALUES: set[IdentityProviderLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_identity_provider_last_state(value: str) -> IdentityProviderLastState:
    if value in IDENTITY_PROVIDER_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_LAST_STATE_VALUES!r}")
