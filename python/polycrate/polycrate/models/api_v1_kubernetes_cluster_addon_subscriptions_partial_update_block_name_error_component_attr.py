from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockNameErrorComponentAttr = Literal["block_name"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockNameErrorComponentAttr
] = {
    "block_name",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_block_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
