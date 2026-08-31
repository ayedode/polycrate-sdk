from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_backups_backup_schedules_partial_update_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
