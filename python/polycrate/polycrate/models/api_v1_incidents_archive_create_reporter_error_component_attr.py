from typing import Literal

ApiV1IncidentsArchiveCreateReporterErrorComponentAttr = Literal["reporter"]

API_V1_INCIDENTS_ARCHIVE_CREATE_REPORTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateReporterErrorComponentAttr
] = {
    "reporter",
}


def check_api_v1_incidents_archive_create_reporter_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateReporterErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_REPORTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_REPORTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
