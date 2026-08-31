from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
