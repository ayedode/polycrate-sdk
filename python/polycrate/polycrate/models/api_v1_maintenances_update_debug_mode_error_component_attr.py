from typing import Literal

ApiV1MaintenancesUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_MAINTENANCES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_maintenances_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateDebugModeErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
