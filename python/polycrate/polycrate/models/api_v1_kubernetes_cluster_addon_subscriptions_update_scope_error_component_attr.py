from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsUpdateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_update_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsUpdateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
