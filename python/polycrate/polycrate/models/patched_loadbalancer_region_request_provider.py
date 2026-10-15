from typing import Literal

PatchedLoadbalancerRegionRequestProvider = Literal[
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

PATCHED_LOADBALANCER_REGION_REQUEST_PROVIDER_VALUES: set[PatchedLoadbalancerRegionRequestProvider] = {
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


def check_patched_loadbalancer_region_request_provider(value: str) -> PatchedLoadbalancerRegionRequestProvider:
    if value in PATCHED_LOADBALANCER_REGION_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_LOADBALANCER_REGION_REQUEST_PROVIDER_VALUES!r}"
    )
