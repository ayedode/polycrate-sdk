from typing import Literal

ApiV1BlocksCheckCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_CHECK_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCheckCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_check_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreateDebugModeErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
