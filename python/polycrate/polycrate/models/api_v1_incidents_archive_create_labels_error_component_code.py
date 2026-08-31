from typing import Literal

ApiV1IncidentsArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_INCIDENTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_incidents_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1IncidentsArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
