from typing import Literal

ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_BACKUPS_BACKUPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_backups_backups_update_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
