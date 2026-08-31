from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_update_kind_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
