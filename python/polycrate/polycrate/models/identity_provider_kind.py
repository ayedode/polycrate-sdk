from typing import Literal

IdentityProviderKind = Literal["authentik", "generic", "keycloak"]

IDENTITY_PROVIDER_KIND_VALUES: set[IdentityProviderKind] = {
    "authentik",
    "generic",
    "keycloak",
}


def check_identity_provider_kind(value: str) -> IdentityProviderKind:
    if value in IDENTITY_PROVIDER_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_KIND_VALUES!r}")
