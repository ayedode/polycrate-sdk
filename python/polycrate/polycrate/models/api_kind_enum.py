from typing import Literal

ApiKindEnum = Literal["cloudflare", "hetzner_cloud", "ionos", "openai_compat", "openstack", "ovhcloud", "proxmox"]

API_KIND_ENUM_VALUES: set[ApiKindEnum] = {
    "cloudflare",
    "hetzner_cloud",
    "ionos",
    "openai_compat",
    "openstack",
    "ovhcloud",
    "proxmox",
}


def check_api_kind_enum(value: str) -> ApiKindEnum:
    if value in API_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_KIND_ENUM_VALUES!r}")
