from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsListState
] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_list_state(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsListState:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_LIST_STATE_VALUES!r}"
    )
