from typing import Literal

ApiV1DatasourcesPartialUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesPartialUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_partial_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1DatasourcesPartialUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
