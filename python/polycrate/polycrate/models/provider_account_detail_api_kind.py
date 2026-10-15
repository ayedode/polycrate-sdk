from typing import Literal

ProviderAccountDetailApiKind = Literal[
    "cloudflare", "hetzner_cloud", "ionos", "openai_compat", "openstack", "ovhcloud", "proxmox"
]

PROVIDER_ACCOUNT_DETAIL_API_KIND_VALUES: set[ProviderAccountDetailApiKind] = {
    "cloudflare",
    "hetzner_cloud",
    "ionos",
    "openai_compat",
    "openstack",
    "ovhcloud",
    "proxmox",
}


def check_provider_account_detail_api_kind(value: str) -> ProviderAccountDetailApiKind:
    if value in PROVIDER_ACCOUNT_DETAIL_API_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_DETAIL_API_KIND_VALUES!r}")
