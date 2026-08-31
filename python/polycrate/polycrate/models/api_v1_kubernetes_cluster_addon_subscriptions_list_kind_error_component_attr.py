from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
