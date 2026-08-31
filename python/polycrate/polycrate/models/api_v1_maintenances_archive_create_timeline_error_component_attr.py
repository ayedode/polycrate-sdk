from typing import Literal

ApiV1MaintenancesArchiveCreateTimelineErrorComponentAttr = Literal["timeline"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_TIMELINE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateTimelineErrorComponentAttr
] = {
    "timeline",
}


def check_api_v1_maintenances_archive_create_timeline_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateTimelineErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_TIMELINE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_TIMELINE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
