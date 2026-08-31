from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
