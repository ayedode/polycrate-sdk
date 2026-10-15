from typing import Literal

PatchedK8SClusterAddonSubscriptionDetailRequestScope = Literal["system", "user"]

PATCHED_K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_SCOPE_VALUES: set[
    PatchedK8SClusterAddonSubscriptionDetailRequestScope
] = {
    "system",
    "user",
}


def check_patched_k8s_cluster_addon_subscription_detail_request_scope(
    value: str,
) -> PatchedK8SClusterAddonSubscriptionDetailRequestScope:
    if value in PATCHED_K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_SCOPE_VALUES!r}"
    )
