from typing import Literal

ParseErrorCodeEnum = Literal["parse_error"]

PARSE_ERROR_CODE_ENUM_VALUES: set[ParseErrorCodeEnum] = {
    "parse_error",
}


def check_parse_error_code_enum(value: str) -> ParseErrorCodeEnum:
    if value in PARSE_ERROR_CODE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PARSE_ERROR_CODE_ENUM_VALUES!r}")
