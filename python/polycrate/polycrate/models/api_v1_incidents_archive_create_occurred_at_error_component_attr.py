from typing import Literal

ApiV1IncidentsArchiveCreateOccurredAtErrorComponentAttr = Literal["occurred_at"]

API_V1_INCIDENTS_ARCHIVE_CREATE_OCCURRED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateOccurredAtErrorComponentAttr
] = {
    "occurred_at",
}


def check_api_v1_incidents_archive_create_occurred_at_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateOccurredAtErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_OCCURRED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_OCCURRED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
