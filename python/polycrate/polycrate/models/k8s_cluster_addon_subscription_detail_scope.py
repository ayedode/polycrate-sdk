from typing import Literal

K8SClusterAddonSubscriptionDetailScope = Literal["system", "user"]

K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_SCOPE_VALUES: set[K8SClusterAddonSubscriptionDetailScope] = {
    "system",
    "user",
}


def check_k8s_cluster_addon_subscription_detail_scope(value: str) -> K8SClusterAddonSubscriptionDetailScope:
    if value in K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_SCOPE_VALUES!r}"
    )
