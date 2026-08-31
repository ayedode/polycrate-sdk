from typing import Literal

ApiV1CvesUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_CVES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateDebugModeErrorComponentAttr] = {
    "debug_mode",
}


def check_api_v1_cves_update_debug_mode_error_component_attr(value: str) -> ApiV1CvesUpdateDebugModeErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
