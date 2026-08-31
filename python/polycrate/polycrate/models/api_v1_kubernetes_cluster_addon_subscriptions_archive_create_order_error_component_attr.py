from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateOrderErrorComponentAttr = Literal["order"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_ORDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateOrderErrorComponentAttr
] = {
    "order",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_order_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateOrderErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_ORDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_ORDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
