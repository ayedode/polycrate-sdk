from typing import Literal

ApiV1DatasourcesSyncCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_SYNC_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesSyncCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_sync_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1DatasourcesSyncCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_DATASOURCES_SYNC_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
