from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListTimeRangeErrorComponentAttr
] = {
    "time_range",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_time_range_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListTimeRangeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
