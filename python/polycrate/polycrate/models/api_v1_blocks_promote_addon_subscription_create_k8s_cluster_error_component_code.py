from typing import Literal

ApiV1BlocksPromoteAddonSubscriptionCreateK8SClusterErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPromoteAddonSubscriptionCreateK8SClusterErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_promote_addon_subscription_create_k8s_cluster_error_component_code(
    value: str,
) -> ApiV1BlocksPromoteAddonSubscriptionCreateK8SClusterErrorComponentCode:
    if value in API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
