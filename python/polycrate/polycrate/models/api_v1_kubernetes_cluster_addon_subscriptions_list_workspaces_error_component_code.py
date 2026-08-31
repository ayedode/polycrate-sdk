from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListWorkspacesErrorComponentCode = Literal[
    "invalid_choice", "invalid_list", "invalid_pk_value"
]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListWorkspacesErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_workspaces_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListWorkspacesErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
