from typing import Literal

ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_RECONCILE_CREATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_reconcile_create_has_incompatible_kubeconfig_error_component_code(
    value: str,
) -> ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponentCode:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
