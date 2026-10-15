from typing import Literal

IdentityProviderRequestSyncMode = Literal["disabled", "full", "pull", "push"]

IDENTITY_PROVIDER_REQUEST_SYNC_MODE_VALUES: set[IdentityProviderRequestSyncMode] = {
    "disabled",
    "full",
    "pull",
    "push",
}


def check_identity_provider_request_sync_mode(value: str) -> IdentityProviderRequestSyncMode:
    if value in IDENTITY_PROVIDER_REQUEST_SYNC_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_REQUEST_SYNC_MODE_VALUES!r}")
