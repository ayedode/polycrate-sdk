from typing import Literal

ApiV1IncidentsArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_INCIDENTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_incidents_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1IncidentsArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
