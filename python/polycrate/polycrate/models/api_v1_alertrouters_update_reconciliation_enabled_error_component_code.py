from typing import Literal

ApiV1AlertroutersUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTROUTERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertrouters_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1AlertroutersUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ALERTROUTERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
