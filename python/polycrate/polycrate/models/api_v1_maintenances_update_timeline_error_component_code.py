from typing import Literal

ApiV1MaintenancesUpdateTimelineErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_UPDATE_TIMELINE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesUpdateTimelineErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_update_timeline_error_component_code(
    value: str,
) -> ApiV1MaintenancesUpdateTimelineErrorComponentCode:
    if value in API_V1_MAINTENANCES_UPDATE_TIMELINE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_TIMELINE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
