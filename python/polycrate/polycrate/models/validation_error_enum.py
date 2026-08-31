from typing import Literal

ValidationErrorEnum = Literal["validation_error"]

VALIDATION_ERROR_ENUM_VALUES: set[ValidationErrorEnum] = {
    "validation_error",
}


def check_validation_error_enum(value: str) -> ValidationErrorEnum:
    if value in VALIDATION_ERROR_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VALIDATION_ERROR_ENUM_VALUES!r}")
