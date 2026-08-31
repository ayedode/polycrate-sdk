from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListScope = Literal["system", "user"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SCOPE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListScope
] = {
    "system",
    "user",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_scope(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListScope:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_SCOPE_VALUES!r}"
    )
