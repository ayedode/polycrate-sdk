from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_update_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
