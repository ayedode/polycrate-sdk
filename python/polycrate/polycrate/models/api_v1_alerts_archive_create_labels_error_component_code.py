from typing import Literal

ApiV1AlertsArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ALERTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_alerts_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1AlertsArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
