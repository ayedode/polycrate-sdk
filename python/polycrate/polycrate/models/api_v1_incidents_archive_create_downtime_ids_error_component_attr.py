from typing import Literal

ApiV1IncidentsArchiveCreateDowntimeIdsErrorComponentAttr = Literal["downtime_ids"]

API_V1_INCIDENTS_ARCHIVE_CREATE_DOWNTIME_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateDowntimeIdsErrorComponentAttr
] = {
    "downtime_ids",
}


def check_api_v1_incidents_archive_create_downtime_ids_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateDowntimeIdsErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_DOWNTIME_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_DOWNTIME_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
