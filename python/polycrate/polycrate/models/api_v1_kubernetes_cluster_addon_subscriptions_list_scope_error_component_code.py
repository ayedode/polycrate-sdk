from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
