from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateOrderErrorComponentAttr = Literal["order"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_ORDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateOrderErrorComponentAttr
] = {
    "order",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_order_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateOrderErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_ORDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_ORDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
