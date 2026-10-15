from typing import Literal

PatchedIdentityProviderRequestKind = Literal["authentik", "generic", "keycloak"]

PATCHED_IDENTITY_PROVIDER_REQUEST_KIND_VALUES: set[PatchedIdentityProviderRequestKind] = {
    "authentik",
    "generic",
    "keycloak",
}


def check_patched_identity_provider_request_kind(value: str) -> PatchedIdentityProviderRequestKind:
    if value in PATCHED_IDENTITY_PROVIDER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_IDENTITY_PROVIDER_REQUEST_KIND_VALUES!r}")
