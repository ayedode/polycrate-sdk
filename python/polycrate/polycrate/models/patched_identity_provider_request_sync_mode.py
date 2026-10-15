from typing import Literal

PatchedIdentityProviderRequestSyncMode = Literal["disabled", "full", "pull", "push"]

PATCHED_IDENTITY_PROVIDER_REQUEST_SYNC_MODE_VALUES: set[PatchedIdentityProviderRequestSyncMode] = {
    "disabled",
    "full",
    "pull",
    "push",
}


def check_patched_identity_provider_request_sync_mode(value: str) -> PatchedIdentityProviderRequestSyncMode:
    if value in PATCHED_IDENTITY_PROVIDER_REQUEST_SYNC_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_IDENTITY_PROVIDER_REQUEST_SYNC_MODE_VALUES!r}"
    )
