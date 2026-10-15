from typing import Literal

PatchedK8SClusterRequestProvider = Literal[
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

PATCHED_K8S_CLUSTER_REQUEST_PROVIDER_VALUES: set[PatchedK8SClusterRequestProvider] = {
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


def check_patched_k8s_cluster_request_provider(value: str) -> PatchedK8SClusterRequestProvider:
    if value in PATCHED_K8S_CLUSTER_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_CLUSTER_REQUEST_PROVIDER_VALUES!r}")
