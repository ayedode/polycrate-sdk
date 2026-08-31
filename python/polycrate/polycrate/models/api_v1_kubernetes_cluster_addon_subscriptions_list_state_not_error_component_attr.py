from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_state_not_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListStateNotErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
