from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_NOT_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListStateNot
] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_state_not(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListStateNot:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_NOT_VALUES!r}"
    )
