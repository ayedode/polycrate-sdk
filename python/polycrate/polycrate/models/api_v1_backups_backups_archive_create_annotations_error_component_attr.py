from typing import Literal

ApiV1BackupsBackupsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_backups_backups_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
