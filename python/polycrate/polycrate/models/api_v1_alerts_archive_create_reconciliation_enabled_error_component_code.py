from typing import Literal

ApiV1AlertsArchiveCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsArchiveCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alerts_archive_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1AlertsArchiveCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
