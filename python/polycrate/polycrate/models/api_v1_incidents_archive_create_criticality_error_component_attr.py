from typing import Literal

ApiV1IncidentsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_INCIDENTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_incidents_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
