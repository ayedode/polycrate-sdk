from typing import Literal

SystemAPIKeyRequestAccessModeType1 = Literal["", "read", "read_write"]

SYSTEM_API_KEY_REQUEST_ACCESS_MODE_TYPE_1_VALUES: set[SystemAPIKeyRequestAccessModeType1] = {
    "",
    "read",
    "read_write",
}


def check_system_api_key_request_access_mode_type_1(value: str) -> SystemAPIKeyRequestAccessModeType1:
    if value in SYSTEM_API_KEY_REQUEST_ACCESS_MODE_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SYSTEM_API_KEY_REQUEST_ACCESS_MODE_TYPE_1_VALUES!r}")
