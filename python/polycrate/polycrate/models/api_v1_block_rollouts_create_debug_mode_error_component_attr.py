from typing import Literal

ApiV1BlockRolloutsCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_BLOCK_ROLLOUTS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_block_rollouts_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateDebugModeErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
