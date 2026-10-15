from typing import Literal

CredentialScope = Literal["system", "user"]

CREDENTIAL_SCOPE_VALUES: set[CredentialScope] = {
    "system",
    "user",
}


def check_credential_scope(value: str) -> CredentialScope:
    if value in CREDENTIAL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_SCOPE_VALUES!r}")
