from typing import Literal

ApiV1WorkspacesReconcileCreateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_RECONCILE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReconcileCreateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_reconcile_create_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesReconcileCreateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
