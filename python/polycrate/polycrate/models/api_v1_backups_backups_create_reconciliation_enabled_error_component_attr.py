from typing import Literal

ApiV1BackupsBackupsCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_BACKUPS_BACKUPS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_backups_backups_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
