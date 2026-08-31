from typing import Literal

ClientErrorEnum = Literal["client_error"]

CLIENT_ERROR_ENUM_VALUES: set[ClientErrorEnum] = {
    "client_error",
}


def check_client_error_enum(value: str) -> ClientErrorEnum:
    if value in CLIENT_ERROR_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLIENT_ERROR_ENUM_VALUES!r}")
