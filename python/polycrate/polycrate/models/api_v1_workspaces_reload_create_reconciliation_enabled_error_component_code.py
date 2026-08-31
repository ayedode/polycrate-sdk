from typing import Literal

ApiV1WorkspacesReloadCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_RELOAD_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReloadCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_reload_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesReloadCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
