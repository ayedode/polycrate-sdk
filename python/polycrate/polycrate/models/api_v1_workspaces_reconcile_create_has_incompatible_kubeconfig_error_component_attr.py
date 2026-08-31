from typing import Literal

ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponentAttr = Literal["has_incompatible_kubeconfig"]

API_V1_WORKSPACES_RECONCILE_CREATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponentAttr
] = {
    "has_incompatible_kubeconfig",
}


def check_api_v1_workspaces_reconcile_create_has_incompatible_kubeconfig_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReconcileCreateHasIncompatibleKubeconfigErrorComponentAttr:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
