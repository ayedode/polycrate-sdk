from typing import Literal

ApiV1BackupsBackupSchedulesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_backups_backup_schedules_create_kind_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateKindErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
