from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
