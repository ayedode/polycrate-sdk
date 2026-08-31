from typing import Literal

ApiV1SystemApiKeysCreateAccessModeErrorComponentCode = Literal["invalid_choice"]

API_V1_SYSTEM_API_KEYS_CREATE_ACCESS_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SystemApiKeysCreateAccessModeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_system_api_keys_create_access_mode_error_component_code(
    value: str,
) -> ApiV1SystemApiKeysCreateAccessModeErrorComponentCode:
    if value in API_V1_SYSTEM_API_KEYS_CREATE_ACCESS_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SYSTEM_API_KEYS_CREATE_ACCESS_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
