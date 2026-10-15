from typing import Literal

ProviderAccountListApiKind = Literal[
    "cloudflare", "hetzner_cloud", "ionos", "openai_compat", "openstack", "ovhcloud", "proxmox"
]

PROVIDER_ACCOUNT_LIST_API_KIND_VALUES: set[ProviderAccountListApiKind] = {
    "cloudflare",
    "hetzner_cloud",
    "ionos",
    "openai_compat",
    "openstack",
    "ovhcloud",
    "proxmox",
}


def check_provider_account_list_api_kind(value: str) -> ProviderAccountListApiKind:
    if value in PROVIDER_ACCOUNT_LIST_API_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_LIST_API_KIND_VALUES!r}")
