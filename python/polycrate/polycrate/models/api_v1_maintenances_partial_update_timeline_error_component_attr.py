from typing import Literal

ApiV1MaintenancesPartialUpdateTimelineErrorComponentAttr = Literal["timeline"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_TIMELINE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateTimelineErrorComponentAttr
] = {
    "timeline",
}


def check_api_v1_maintenances_partial_update_timeline_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateTimelineErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_TIMELINE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_TIMELINE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
