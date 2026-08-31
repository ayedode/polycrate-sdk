from typing import Literal

ApiV1BackupsBackupSchedulesCreateNameErrorComponentAttr = Literal["name"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_backups_backup_schedules_create_name_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateNameErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
