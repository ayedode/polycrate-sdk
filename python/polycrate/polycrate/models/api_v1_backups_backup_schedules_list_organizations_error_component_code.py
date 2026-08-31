from typing import Literal

ApiV1BackupsBackupSchedulesListOrganizationsErrorComponentCode = Literal[
    "invalid_choice", "invalid_list", "invalid_pk_value"
]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesListOrganizationsErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_backups_backup_schedules_list_organizations_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesListOrganizationsErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
