from typing import Literal

ErrorCode409Enum = Literal["action_run_already_running", "conflict"]

ERROR_CODE_409_ENUM_VALUES: set[ErrorCode409Enum] = {
    "action_run_already_running",
    "conflict",
}


def check_error_code_409_enum(value: str) -> ErrorCode409Enum:
    if value in ERROR_CODE_409_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_CODE_409_ENUM_VALUES!r}")
