from typing import Literal

K8SClusterAddonSubscriptionDetailRequestKind = Literal["generic"]

K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_KIND_VALUES: set[K8SClusterAddonSubscriptionDetailRequestKind] = {
    "generic",
}


def check_k8s_cluster_addon_subscription_detail_request_kind(
    value: str,
) -> K8SClusterAddonSubscriptionDetailRequestKind:
    if value in K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_KIND_VALUES!r}"
    )
