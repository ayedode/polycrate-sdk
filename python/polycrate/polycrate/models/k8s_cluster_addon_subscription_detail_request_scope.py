from typing import Literal

K8SClusterAddonSubscriptionDetailRequestScope = Literal["system", "user"]

K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_SCOPE_VALUES: set[K8SClusterAddonSubscriptionDetailRequestScope] = {
    "system",
    "user",
}


def check_k8s_cluster_addon_subscription_detail_request_scope(
    value: str,
) -> K8SClusterAddonSubscriptionDetailRequestScope:
    if value in K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_SCOPE_VALUES!r}"
    )
