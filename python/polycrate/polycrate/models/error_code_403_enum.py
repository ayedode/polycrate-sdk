from typing import Literal

ErrorCode403Enum = Literal["permission_denied"]

ERROR_CODE_403_ENUM_VALUES: set[ErrorCode403Enum] = {
    "permission_denied",
}


def check_error_code_403_enum(value: str) -> ErrorCode403Enum:
    if value in ERROR_CODE_403_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_CODE_403_ENUM_VALUES!r}")
