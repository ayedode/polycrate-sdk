from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListKindItem = Literal["generic"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_KIND_ITEM_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListKindItem
] = {
    "generic",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_kind_item(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListKindItem:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_KIND_ITEM_VALUES!r}"
    )
