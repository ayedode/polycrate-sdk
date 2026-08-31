from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsCreateAddonErrorComponentAttr = Literal["addon"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_ADDON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsCreateAddonErrorComponentAttr
] = {
    "addon",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_create_addon_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsCreateAddonErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_ADDON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_ADDON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
