from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_create_criticality_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsCreateCriticalityErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
