from typing import Literal

PatchedProviderAccountDetailRequestApiKind = Literal[
    "cloudflare", "hetzner_cloud", "ionos", "openai_compat", "openstack", "ovhcloud", "proxmox"
]

PATCHED_PROVIDER_ACCOUNT_DETAIL_REQUEST_API_KIND_VALUES: set[PatchedProviderAccountDetailRequestApiKind] = {
    "cloudflare",
    "hetzner_cloud",
    "ionos",
    "openai_compat",
    "openstack",
    "ovhcloud",
    "proxmox",
}


def check_patched_provider_account_detail_request_api_kind(value: str) -> PatchedProviderAccountDetailRequestApiKind:
    if value in PATCHED_PROVIDER_ACCOUNT_DETAIL_REQUEST_API_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_ACCOUNT_DETAIL_REQUEST_API_KIND_VALUES!r}"
    )
