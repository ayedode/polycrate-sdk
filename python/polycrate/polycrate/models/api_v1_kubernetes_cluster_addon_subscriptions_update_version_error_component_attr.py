from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsUpdateVersionErrorComponentAttr = Literal["version"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsUpdateVersionErrorComponentAttr
] = {
    "version",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_update_version_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsUpdateVersionErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
