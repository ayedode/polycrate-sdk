from typing import Literal

ApiV1DatasourcesRescanNotesCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_rescan_notes_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
