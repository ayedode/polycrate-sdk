from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsCreateBlockNameErrorComponentAttr = Literal["block_name"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsCreateBlockNameErrorComponentAttr
] = {
    "block_name",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_create_block_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsCreateBlockNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
