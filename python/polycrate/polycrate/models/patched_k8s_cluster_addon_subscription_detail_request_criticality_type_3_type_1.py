from typing import Literal

PatchedK8SClusterAddonSubscriptionDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedK8SClusterAddonSubscriptionDetailRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_k8s_cluster_addon_subscription_detail_request_criticality_type_3_type_1(
    value: str,
) -> PatchedK8SClusterAddonSubscriptionDetailRequestCriticalityType3Type1:
    if value in PATCHED_K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
