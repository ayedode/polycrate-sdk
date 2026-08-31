from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsPartialUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsPartialUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_platform_service_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsPartialUpdatePlatformServiceErrorComponentCode:
    if (
        value
        in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
