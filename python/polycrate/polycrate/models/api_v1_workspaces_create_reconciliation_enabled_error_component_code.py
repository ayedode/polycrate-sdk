from typing import Literal

ApiV1WorkspacesCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
