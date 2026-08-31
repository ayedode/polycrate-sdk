from typing import Literal

ApiV1BlocksRepairCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_BLOCKS_REPAIR_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_blocks_repair_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateDebugModeErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
