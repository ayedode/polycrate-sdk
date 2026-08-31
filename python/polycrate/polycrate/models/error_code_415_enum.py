from typing import Literal

ErrorCode415Enum = Literal["unsupported_media_type"]

ERROR_CODE_415_ENUM_VALUES: set[ErrorCode415Enum] = {
    "unsupported_media_type",
}


def check_error_code_415_enum(value: str) -> ErrorCode415Enum:
    if value in ERROR_CODE_415_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_CODE_415_ENUM_VALUES!r}")
