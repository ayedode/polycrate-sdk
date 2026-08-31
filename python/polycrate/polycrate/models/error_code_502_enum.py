from typing import Literal

ErrorCode502Enum = Literal["provider_bad_gateway", "provider_object_creation_failed"]

ERROR_CODE_502_ENUM_VALUES: set[ErrorCode502Enum] = {
    "provider_bad_gateway",
    "provider_object_creation_failed",
}


def check_error_code_502_enum(value: str) -> ErrorCode502Enum:
    if value in ERROR_CODE_502_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_CODE_502_ENUM_VALUES!r}")
