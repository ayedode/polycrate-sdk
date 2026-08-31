from typing import Literal

ServerErrorEnum = Literal["server_error"]

SERVER_ERROR_ENUM_VALUES: set[ServerErrorEnum] = {
    "server_error",
}


def check_server_error_enum(value: str) -> ServerErrorEnum:
    if value in SERVER_ERROR_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVER_ERROR_ENUM_VALUES!r}")
