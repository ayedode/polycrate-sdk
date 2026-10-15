from typing import Literal

ProviderAccountDetailRequestApiKind = Literal[
    "cloudflare", "hetzner_cloud", "ionos", "openai_compat", "openstack", "ovhcloud", "proxmox"
]

PROVIDER_ACCOUNT_DETAIL_REQUEST_API_KIND_VALUES: set[ProviderAccountDetailRequestApiKind] = {
    "cloudflare",
    "hetzner_cloud",
    "ionos",
    "openai_compat",
    "openstack",
    "ovhcloud",
    "proxmox",
}


def check_provider_account_detail_request_api_kind(value: str) -> ProviderAccountDetailRequestApiKind:
    if value in PROVIDER_ACCOUNT_DETAIL_REQUEST_API_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_DETAIL_REQUEST_API_KIND_VALUES!r}")
