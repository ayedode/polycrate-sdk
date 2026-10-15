from typing import Literal

LoadbalancerRegionRequestProvider = Literal[
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

LOADBALANCER_REGION_REQUEST_PROVIDER_VALUES: set[LoadbalancerRegionRequestProvider] = {
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


def check_loadbalancer_region_request_provider(value: str) -> LoadbalancerRegionRequestProvider:
    if value in LOADBALANCER_REGION_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_REQUEST_PROVIDER_VALUES!r}")
