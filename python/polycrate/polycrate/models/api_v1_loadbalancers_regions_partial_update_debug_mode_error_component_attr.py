from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_loadbalancers_regions_partial_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdateDebugModeErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
