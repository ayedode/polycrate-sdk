from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_update_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
