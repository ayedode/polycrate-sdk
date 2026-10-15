from typing import Literal

IdentityProviderScope = Literal["system", "user"]

IDENTITY_PROVIDER_SCOPE_VALUES: set[IdentityProviderScope] = {
    "system",
    "user",
}


def check_identity_provider_scope(value: str) -> IdentityProviderScope:
    if value in IDENTITY_PROVIDER_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_SCOPE_VALUES!r}")
