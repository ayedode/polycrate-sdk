from typing import Literal

ApiV1BlockRolloutsUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_BLOCK_ROLLOUTS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_block_rollouts_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateDebugModeErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
