from typing import Literal

ApiV1KubernetesClustersListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_KUBERNETES_CLUSTERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_kubernetes_clusters_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersListWorkspacesErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
