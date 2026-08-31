from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateTimelineErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_TIMELINE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateTimelineErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_complete_early_create_timeline_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateTimelineErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_TIMELINE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_TIMELINE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
