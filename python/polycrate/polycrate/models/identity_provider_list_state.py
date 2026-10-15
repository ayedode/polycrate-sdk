from typing import Literal

IdentityProviderListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

IDENTITY_PROVIDER_LIST_STATE_VALUES: set[IdentityProviderListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_identity_provider_list_state(value: str) -> IdentityProviderListState:
    if value in IDENTITY_PROVIDER_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_LIST_STATE_VALUES!r}")
