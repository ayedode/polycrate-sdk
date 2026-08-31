from typing import Literal

ApiV1BackupsBackupsArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_backups_backups_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
