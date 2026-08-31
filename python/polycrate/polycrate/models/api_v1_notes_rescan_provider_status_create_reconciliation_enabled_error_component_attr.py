from typing import Literal

ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_notes_rescan_provider_status_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
