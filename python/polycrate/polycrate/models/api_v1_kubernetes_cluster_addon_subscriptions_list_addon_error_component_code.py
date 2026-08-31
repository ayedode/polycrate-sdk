from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_ADDON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_addon_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListAddonErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_ADDON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_ADDON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
