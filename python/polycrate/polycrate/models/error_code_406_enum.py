from typing import Literal

ErrorCode406Enum = Literal["not_acceptable"]

ERROR_CODE_406_ENUM_VALUES: set[ErrorCode406Enum] = {
    "not_acceptable",
}


def check_error_code_406_enum(value: str) -> ErrorCode406Enum:
    if value in ERROR_CODE_406_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_CODE_406_ENUM_VALUES!r}")
