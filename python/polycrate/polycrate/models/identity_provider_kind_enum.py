from typing import Literal

IdentityProviderKindEnum = Literal["authentik", "generic", "keycloak"]

IDENTITY_PROVIDER_KIND_ENUM_VALUES: set[IdentityProviderKindEnum] = {
    "authentik",
    "generic",
    "keycloak",
}


def check_identity_provider_kind_enum(value: str) -> IdentityProviderKindEnum:
    if value in IDENTITY_PROVIDER_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_KIND_ENUM_VALUES!r}")
