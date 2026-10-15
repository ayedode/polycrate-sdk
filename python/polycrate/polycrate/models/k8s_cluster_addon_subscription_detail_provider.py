from typing import Literal

K8SClusterAddonSubscriptionDetailProvider = Literal[
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

K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_PROVIDER_VALUES: set[K8SClusterAddonSubscriptionDetailProvider] = {
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


def check_k8s_cluster_addon_subscription_detail_provider(value: str) -> K8SClusterAddonSubscriptionDetailProvider:
    if value in K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_CLUSTER_ADDON_SUBSCRIPTION_DETAIL_PROVIDER_VALUES!r}"
    )
