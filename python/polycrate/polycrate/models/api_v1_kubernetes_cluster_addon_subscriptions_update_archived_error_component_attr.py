from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_update_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
