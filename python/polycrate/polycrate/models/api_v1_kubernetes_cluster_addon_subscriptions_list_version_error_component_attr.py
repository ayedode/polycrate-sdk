from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListVersionErrorComponentAttr = Literal["version"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListVersionErrorComponentAttr
] = {
    "version",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_version_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListVersionErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
