from typing import Literal

ApiV1BlockRolloutsPartialUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollouts_partial_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateDebugModeErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
