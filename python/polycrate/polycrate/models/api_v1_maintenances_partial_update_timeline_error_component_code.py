from typing import Literal

ApiV1MaintenancesPartialUpdateTimelineErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_TIMELINE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesPartialUpdateTimelineErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_partial_update_timeline_error_component_code(
    value: str,
) -> ApiV1MaintenancesPartialUpdateTimelineErrorComponentCode:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_TIMELINE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_TIMELINE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
