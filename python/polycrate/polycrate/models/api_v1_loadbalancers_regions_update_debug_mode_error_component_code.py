from typing import Literal

ApiV1LoadbalancersRegionsUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_regions_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateDebugModeErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
