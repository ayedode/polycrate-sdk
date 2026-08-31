from typing import Literal

ErrorCode405Enum = Literal["method_not_allowed"]

ERROR_CODE_405_ENUM_VALUES: set[ErrorCode405Enum] = {
    "method_not_allowed",
}


def check_error_code_405_enum(value: str) -> ErrorCode405Enum:
    if value in ERROR_CODE_405_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_CODE_405_ENUM_VALUES!r}")
