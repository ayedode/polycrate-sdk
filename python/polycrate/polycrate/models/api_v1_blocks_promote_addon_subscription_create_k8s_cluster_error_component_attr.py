from typing import Literal

ApiV1BlocksPromoteAddonSubscriptionCreateK8SClusterErrorComponentAttr = Literal["k8s_cluster"]

API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPromoteAddonSubscriptionCreateK8SClusterErrorComponentAttr
] = {
    "k8s_cluster",
}


def check_api_v1_blocks_promote_addon_subscription_create_k8s_cluster_error_component_attr(
    value: str,
) -> ApiV1BlocksPromoteAddonSubscriptionCreateK8SClusterErrorComponentAttr:
    if value in API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
