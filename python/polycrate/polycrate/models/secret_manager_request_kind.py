from typing import Literal

SecretManagerRequestKind = Literal["vault"]

SECRET_MANAGER_REQUEST_KIND_VALUES: set[SecretManagerRequestKind] = {
    "vault",
}


def check_secret_manager_request_kind(value: str) -> SecretManagerRequestKind:
    if value in SECRET_MANAGER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_REQUEST_KIND_VALUES!r}")
