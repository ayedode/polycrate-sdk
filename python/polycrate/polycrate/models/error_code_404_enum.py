from typing import Literal

ErrorCode404Enum = Literal["not_found"]

ERROR_CODE_404_ENUM_VALUES: set[ErrorCode404Enum] = {
    "not_found",
}


def check_error_code_404_enum(value: str) -> ErrorCode404Enum:
    if value in ERROR_CODE_404_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_CODE_404_ENUM_VALUES!r}")
