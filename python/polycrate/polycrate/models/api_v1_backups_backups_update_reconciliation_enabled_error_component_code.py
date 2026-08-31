from typing import Literal

ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backups_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
