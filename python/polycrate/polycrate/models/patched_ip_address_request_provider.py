from typing import Literal

PatchedIPAddressRequestProvider = Literal[
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

PATCHED_IP_ADDRESS_REQUEST_PROVIDER_VALUES: set[PatchedIPAddressRequestProvider] = {
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


def check_patched_ip_address_request_provider(value: str) -> PatchedIPAddressRequestProvider:
    if value in PATCHED_IP_ADDRESS_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_IP_ADDRESS_REQUEST_PROVIDER_VALUES!r}")
