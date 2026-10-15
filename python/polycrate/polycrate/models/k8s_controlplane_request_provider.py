from typing import Literal

K8SControlplaneRequestProvider = Literal[
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

K8S_CONTROLPLANE_REQUEST_PROVIDER_VALUES: set[K8SControlplaneRequestProvider] = {
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


def check_k8s_controlplane_request_provider(value: str) -> K8SControlplaneRequestProvider:
    if value in K8S_CONTROLPLANE_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_REQUEST_PROVIDER_VALUES!r}")
