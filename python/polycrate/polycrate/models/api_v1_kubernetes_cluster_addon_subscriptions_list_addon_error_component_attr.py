from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponentAttr = Literal["addon"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_ADDON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponentAttr
] = {
    "addon",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_addon_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_ADDON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_ADDON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
