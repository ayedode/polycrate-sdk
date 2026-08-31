from typing import Literal

ApiV1HostsListProvider = Literal[
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

API_V1_HOSTS_LIST_PROVIDER_VALUES: set[ApiV1HostsListProvider] = {
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


def check_api_v1_hosts_list_provider(value: str) -> ApiV1HostsListProvider:
    if value in API_V1_HOSTS_LIST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_PROVIDER_VALUES!r}")
