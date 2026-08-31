from typing import Literal

ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notes_rescan_provider_status_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
