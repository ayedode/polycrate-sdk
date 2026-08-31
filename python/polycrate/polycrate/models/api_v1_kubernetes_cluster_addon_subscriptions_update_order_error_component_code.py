from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsUpdateOrderErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_ORDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsUpdateOrderErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_update_order_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsUpdateOrderErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_ORDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_ORDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
