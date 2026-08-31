from typing import Literal

ErrorCode500Enum = Literal["error"]

ERROR_CODE_500_ENUM_VALUES: set[ErrorCode500Enum] = {
    "error",
}


def check_error_code_500_enum(value: str) -> ErrorCode500Enum:
    if value in ERROR_CODE_500_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_CODE_500_ENUM_VALUES!r}")
