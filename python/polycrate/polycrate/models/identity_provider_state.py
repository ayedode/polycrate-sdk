from typing import Literal

IdentityProviderState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

IDENTITY_PROVIDER_STATE_VALUES: set[IdentityProviderState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_identity_provider_state(value: str) -> IdentityProviderState:
    if value in IDENTITY_PROVIDER_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_STATE_VALUES!r}")
