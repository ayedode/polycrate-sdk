from typing import Literal

K8SClusterAddonSubscriptionDetailKind = Literal["generic"]

K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_KIND_VALUES: set[K8SClusterAddonSubscriptionDetailKind] = {
    "generic",
}


def check_k8s_cluster_addon_subscription_detail_kind(value: str) -> K8SClusterAddonSubscriptionDetailKind:
    if value in K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_KIND_VALUES!r}"
    )
