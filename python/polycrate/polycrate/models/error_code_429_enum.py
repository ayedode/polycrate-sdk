from typing import Literal

ErrorCode429Enum = Literal["throttled"]

ERROR_CODE_429_ENUM_VALUES: set[ErrorCode429Enum] = {
    "throttled",
}


def check_error_code_429_enum(value: str) -> ErrorCode429Enum:
    if value in ERROR_CODE_429_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_CODE_429_ENUM_VALUES!r}")
