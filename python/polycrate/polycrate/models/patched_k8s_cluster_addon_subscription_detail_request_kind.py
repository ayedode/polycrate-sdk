from typing import Literal

PatchedK8SClusterAddonSubscriptionDetailRequestKind = Literal["generic"]

PATCHED_K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_KIND_VALUES: set[
    PatchedK8SClusterAddonSubscriptionDetailRequestKind
] = {
    "generic",
}


def check_patched_k8s_cluster_addon_subscription_detail_request_kind(
    value: str,
) -> PatchedK8SClusterAddonSubscriptionDetailRequestKind:
    if value in PATCHED_K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_KIND_VALUES!r}"
    )
