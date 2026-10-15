from typing import Literal

K8SClusterAddonSubscriptionListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_CLUSTER_ADDON_SUBSCRIPTION_LIST_STATE_VALUES: set[K8SClusterAddonSubscriptionListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_cluster_addon_subscription_list_state(value: str) -> K8SClusterAddonSubscriptionListState:
    if value in K8S_CLUSTER_ADDON_SUBSCRIPTION_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_ADDON_SUBSCRIPTION_LIST_STATE_VALUES!r}")
