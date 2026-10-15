from typing import Literal

IdentityProviderSyncMode = Literal["disabled", "full", "pull", "push"]

IDENTITY_PROVIDER_SYNC_MODE_VALUES: set[IdentityProviderSyncMode] = {
    "disabled",
    "full",
    "pull",
    "push",
}


def check_identity_provider_sync_mode(value: str) -> IdentityProviderSyncMode:
    if value in IDENTITY_PROVIDER_SYNC_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_SYNC_MODE_VALUES!r}")
