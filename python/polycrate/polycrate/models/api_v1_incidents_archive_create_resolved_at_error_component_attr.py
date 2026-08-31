from typing import Literal

ApiV1IncidentsArchiveCreateResolvedAtErrorComponentAttr = Literal["resolved_at"]

API_V1_INCIDENTS_ARCHIVE_CREATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateResolvedAtErrorComponentAttr
] = {
    "resolved_at",
}


def check_api_v1_incidents_archive_create_resolved_at_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateResolvedAtErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
