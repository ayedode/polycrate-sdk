from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_create_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsCreateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
