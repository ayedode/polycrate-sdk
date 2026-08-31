from typing import Literal

ApiV1BackupsBackupSchedulesUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_backups_backup_schedules_update_archived_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateArchivedErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
