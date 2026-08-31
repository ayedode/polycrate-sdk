from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
