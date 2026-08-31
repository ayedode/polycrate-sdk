from typing import Literal

ApiV1KubernetesAddonsListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_KUBERNETES_ADDONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_kubernetes_addons_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsListWorkspacesErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
