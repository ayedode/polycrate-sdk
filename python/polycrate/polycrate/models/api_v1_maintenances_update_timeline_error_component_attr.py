from typing import Literal

ApiV1MaintenancesUpdateTimelineErrorComponentAttr = Literal["timeline"]

API_V1_MAINTENANCES_UPDATE_TIMELINE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateTimelineErrorComponentAttr
] = {
    "timeline",
}


def check_api_v1_maintenances_update_timeline_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateTimelineErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_TIMELINE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_TIMELINE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
