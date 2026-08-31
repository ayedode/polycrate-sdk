from typing import Literal

ApiV1BackupsBackupSchedulesListSourceNamespaceErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SOURCE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesListSourceNamespaceErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_backups_backup_schedules_list_source_namespace_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesListSourceNamespaceErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SOURCE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SOURCE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
