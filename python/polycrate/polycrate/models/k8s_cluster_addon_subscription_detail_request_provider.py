from typing import Literal

K8SClusterAddonSubscriptionDetailRequestProvider = Literal[
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
]

K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_PROVIDER_VALUES: set[K8SClusterAddonSubscriptionDetailRequestProvider] = {
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
}


def check_k8s_cluster_addon_subscription_detail_request_provider(
    value: str,
) -> K8SClusterAddonSubscriptionDetailRequestProvider:
    if value in K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
