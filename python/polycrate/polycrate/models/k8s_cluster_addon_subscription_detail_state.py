from typing import Literal

K8SClusterAddonSubscriptionDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_STATE_VALUES: set[K8SClusterAddonSubscriptionDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_cluster_addon_subscription_detail_state(value: str) -> K8SClusterAddonSubscriptionDetailState:
    if value in K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_STATE_VALUES!r}"
    )
