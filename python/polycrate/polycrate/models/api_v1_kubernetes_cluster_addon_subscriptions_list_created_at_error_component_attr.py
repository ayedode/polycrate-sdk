from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponentAttr
] = {
    "created_at",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_created_at_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListCreatedAtErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
