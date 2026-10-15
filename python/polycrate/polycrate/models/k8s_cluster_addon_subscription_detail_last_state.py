from typing import Literal

K8SClusterAddonSubscriptionDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_LAST_STATE_VALUES: set[K8SClusterAddonSubscriptionDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_cluster_addon_subscription_detail_last_state(value: str) -> K8SClusterAddonSubscriptionDetailLastState:
    if value in K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_LAST_STATE_VALUES!r}"
    )
