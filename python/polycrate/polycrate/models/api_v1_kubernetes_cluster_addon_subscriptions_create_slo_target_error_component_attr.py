from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsCreateSloTargetErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
