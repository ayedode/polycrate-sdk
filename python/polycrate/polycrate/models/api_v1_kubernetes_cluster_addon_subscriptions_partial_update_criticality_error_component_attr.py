from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
