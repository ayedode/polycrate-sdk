from typing import Literal

ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_backups_backup_schedules_update_annotations_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
