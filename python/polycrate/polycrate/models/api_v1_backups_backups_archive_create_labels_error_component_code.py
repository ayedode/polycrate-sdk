from typing import Literal

ApiV1BackupsBackupsArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_backups_backups_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
