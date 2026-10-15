from typing import Literal

K8SAddonConfigRevisionProvider = Literal[
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

K8S_ADDON_CONFIG_REVISION_PROVIDER_VALUES: set[K8SAddonConfigRevisionProvider] = {
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


def check_k8s_addon_config_revision_provider(value: str) -> K8SAddonConfigRevisionProvider:
    if value in K8S_ADDON_CONFIG_REVISION_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_CONFIG_REVISION_PROVIDER_VALUES!r}")
