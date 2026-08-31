from typing import Literal

ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_backups_backup_schedules_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
