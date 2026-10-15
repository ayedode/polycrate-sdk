from typing import Literal

SecretManagerKind = Literal["vault"]

SECRET_MANAGER_KIND_VALUES: set[SecretManagerKind] = {
    "vault",
}


def check_secret_manager_kind(value: str) -> SecretManagerKind:
    if value in SECRET_MANAGER_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_KIND_VALUES!r}")
