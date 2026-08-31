from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_TIME_RANGE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListTimeRange
] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_time_range(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListTimeRange:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_TIME_RANGE_VALUES!r}"
    )
