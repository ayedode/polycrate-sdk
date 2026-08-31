from typing import Literal

ApiV1DowntimesArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_downtimes_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1DowntimesArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
