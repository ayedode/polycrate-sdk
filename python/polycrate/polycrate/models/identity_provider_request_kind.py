from typing import Literal

IdentityProviderRequestKind = Literal["authentik", "generic", "keycloak"]

IDENTITY_PROVIDER_REQUEST_KIND_VALUES: set[IdentityProviderRequestKind] = {
    "authentik",
    "generic",
    "keycloak",
}


def check_identity_provider_request_kind(value: str) -> IdentityProviderRequestKind:
    if value in IDENTITY_PROVIDER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_REQUEST_KIND_VALUES!r}")
