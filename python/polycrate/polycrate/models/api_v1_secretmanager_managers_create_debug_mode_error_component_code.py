from typing import Literal

ApiV1SecretmanagerManagersCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_secretmanager_managers_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersCreateDebugModeErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
