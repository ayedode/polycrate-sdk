from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
