from typing import Literal

ApiV1WorkspacesUpdateHasIncompatibleKubeconfigErrorComponentAttr = Literal["has_incompatible_kubeconfig"]

API_V1_WORKSPACES_UPDATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateHasIncompatibleKubeconfigErrorComponentAttr
] = {
    "has_incompatible_kubeconfig",
}


def check_api_v1_workspaces_update_has_incompatible_kubeconfig_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateHasIncompatibleKubeconfigErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
