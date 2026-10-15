from typing import Literal

PatchedK8SWorkerPoolRequestProvider = Literal[
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

PATCHED_K8S_WORKER_POOL_REQUEST_PROVIDER_VALUES: set[PatchedK8SWorkerPoolRequestProvider] = {
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


def check_patched_k8s_worker_pool_request_provider(value: str) -> PatchedK8SWorkerPoolRequestProvider:
    if value in PATCHED_K8S_WORKER_POOL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_WORKER_POOL_REQUEST_PROVIDER_VALUES!r}")
