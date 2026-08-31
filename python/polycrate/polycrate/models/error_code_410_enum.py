from typing import Literal

ErrorCode410Enum = Literal["gone"]

ERROR_CODE_410_ENUM_VALUES: set[ErrorCode410Enum] = {
    "gone",
}


def check_error_code_410_enum(value: str) -> ErrorCode410Enum:
    if value in ERROR_CODE_410_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_CODE_410_ENUM_VALUES!r}")
