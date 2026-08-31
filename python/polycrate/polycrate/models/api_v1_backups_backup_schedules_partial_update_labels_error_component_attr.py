from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_backups_backup_schedules_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
