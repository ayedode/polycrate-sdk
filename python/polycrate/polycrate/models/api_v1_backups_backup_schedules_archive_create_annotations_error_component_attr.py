from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_backups_backup_schedules_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
