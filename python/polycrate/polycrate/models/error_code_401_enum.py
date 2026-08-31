from typing import Literal

ErrorCode401Enum = Literal["authentication_failed", "not_authenticated"]

ERROR_CODE_401_ENUM_VALUES: set[ErrorCode401Enum] = {
    "authentication_failed",
    "not_authenticated",
}


def check_error_code_401_enum(value: str) -> ErrorCode401Enum:
    if value in ERROR_CODE_401_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_CODE_401_ENUM_VALUES!r}")
