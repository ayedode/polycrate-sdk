from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaAvailabilityErrorComponentAttr:
    if (
        value
        in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
