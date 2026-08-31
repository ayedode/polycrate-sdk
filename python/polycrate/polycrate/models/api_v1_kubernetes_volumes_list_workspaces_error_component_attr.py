from typing import Literal

ApiV1KubernetesVolumesListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_KUBERNETES_VOLUMES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_kubernetes_volumes_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesListWorkspacesErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
