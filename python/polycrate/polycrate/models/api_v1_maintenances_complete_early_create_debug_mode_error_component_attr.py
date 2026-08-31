from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_maintenances_complete_early_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateDebugModeErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
