from typing import Literal

ApiV1BackupsBackupSchedulesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_backups_backup_schedules_create_annotations_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
