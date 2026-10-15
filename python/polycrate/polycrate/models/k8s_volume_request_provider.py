from typing import Literal

K8SVolumeRequestProvider = Literal[
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

K8S_VOLUME_REQUEST_PROVIDER_VALUES: set[K8SVolumeRequestProvider] = {
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


def check_k8s_volume_request_provider(value: str) -> K8SVolumeRequestProvider:
    if value in K8S_VOLUME_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_REQUEST_PROVIDER_VALUES!r}")
