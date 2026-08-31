from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_created_at_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
