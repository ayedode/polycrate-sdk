from typing import Literal

K8SClusterAddonSubscriptionDetailCriticalityType1 = Literal["", "high", "low", "medium"]

K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_CRITICALITY_TYPE_1_VALUES: set[
    K8SClusterAddonSubscriptionDetailCriticalityType1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_k8s_cluster_addon_subscription_detail_criticality_type_1(
    value: str,
) -> K8SClusterAddonSubscriptionDetailCriticalityType1:
    if value in K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_CRITICALITY_TYPE_1_VALUES!r}"
    )
