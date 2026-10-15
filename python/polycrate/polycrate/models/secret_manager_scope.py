from typing import Literal

SecretManagerScope = Literal["system", "user"]

SECRET_MANAGER_SCOPE_VALUES: set[SecretManagerScope] = {
    "system",
    "user",
}


def check_secret_manager_scope(value: str) -> SecretManagerScope:
    if value in SECRET_MANAGER_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_SCOPE_VALUES!r}")
