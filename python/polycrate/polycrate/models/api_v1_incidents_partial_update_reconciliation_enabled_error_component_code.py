from typing import Literal

ApiV1IncidentsPartialUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_INCIDENTS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsPartialUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_incidents_partial_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1IncidentsPartialUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
