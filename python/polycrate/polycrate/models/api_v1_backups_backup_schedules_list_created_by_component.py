from typing import Literal

ApiV1BackupsBackupSchedulesListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_BY_COMPONENT_VALUES: set[
    ApiV1BackupsBackupSchedulesListCreatedByComponent
] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_backups_backup_schedules_list_created_by_component(
    value: str,
) -> ApiV1BackupsBackupSchedulesListCreatedByComponent:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
