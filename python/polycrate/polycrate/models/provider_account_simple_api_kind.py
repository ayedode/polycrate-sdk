from typing import Literal

ProviderAccountSimpleApiKind = Literal[
    "cloudflare", "hetzner_cloud", "ionos", "openai_compat", "openstack", "ovhcloud", "proxmox"
]

PROVIDER_ACCOUNT_SIMPLE_API_KIND_VALUES: set[ProviderAccountSimpleApiKind] = {
    "cloudflare",
    "hetzner_cloud",
    "ionos",
    "openai_compat",
    "openstack",
    "ovhcloud",
    "proxmox",
}


def check_provider_account_simple_api_kind(value: str) -> ProviderAccountSimpleApiKind:
    if value in PROVIDER_ACCOUNT_SIMPLE_API_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_SIMPLE_API_KIND_VALUES!r}")
