from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListSearchErrorComponentAttr = Literal["search"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_search_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListSearchErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
