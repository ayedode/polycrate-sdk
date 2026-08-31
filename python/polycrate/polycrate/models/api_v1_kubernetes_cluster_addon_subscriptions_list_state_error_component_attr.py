from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListStateErrorComponentAttr = Literal["state"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_state_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListStateErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
