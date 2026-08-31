from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponentCode = Literal["invalid_choice", "invalid_list"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_kind_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
