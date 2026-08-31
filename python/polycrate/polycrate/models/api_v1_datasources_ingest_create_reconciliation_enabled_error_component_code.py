from typing import Literal

ApiV1DatasourcesIngestCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_INGEST_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesIngestCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_ingest_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1DatasourcesIngestCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_DATASOURCES_INGEST_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
