from typing import Literal

LoadbalancerInstanceRequestProvider = Literal[
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

LOADBALANCER_INSTANCE_REQUEST_PROVIDER_VALUES: set[LoadbalancerInstanceRequestProvider] = {
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


def check_loadbalancer_instance_request_provider(value: str) -> LoadbalancerInstanceRequestProvider:
    if value in LOADBALANCER_INSTANCE_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_REQUEST_PROVIDER_VALUES!r}")
