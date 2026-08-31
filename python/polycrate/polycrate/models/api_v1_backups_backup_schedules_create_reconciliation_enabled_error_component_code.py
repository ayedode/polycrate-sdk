from typing import Literal

ApiV1BackupsBackupSchedulesCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backup_schedules_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
