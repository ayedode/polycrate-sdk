from typing import Literal

ApiV1AlertroutersArchiveCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersArchiveCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertrouters_archive_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1AlertroutersArchiveCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
