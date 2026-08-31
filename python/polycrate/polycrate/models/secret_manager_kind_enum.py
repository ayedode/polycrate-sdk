from typing import Literal

SecretManagerKindEnum = Literal["vault"]

SECRET_MANAGER_KIND_ENUM_VALUES: set[SecretManagerKindEnum] = {
    "vault",
}


def check_secret_manager_kind_enum(value: str) -> SecretManagerKindEnum:
    if value in SECRET_MANAGER_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_KIND_ENUM_VALUES!r}")
