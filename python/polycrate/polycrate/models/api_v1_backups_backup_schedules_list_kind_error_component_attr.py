from typing import Literal

ApiV1BackupsBackupSchedulesListKindErrorComponentAttr = Literal["kind"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_backups_backup_schedules_list_kind_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesListKindErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
