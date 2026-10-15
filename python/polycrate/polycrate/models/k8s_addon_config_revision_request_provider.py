from typing import Literal

K8SAddonConfigRevisionRequestProvider = Literal[
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

K8S_ADDON_CONFIG_REVISION_REQUEST_PROVIDER_VALUES: set[K8SAddonConfigRevisionRequestProvider] = {
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


def check_k8s_addon_config_revision_request_provider(value: str) -> K8SAddonConfigRevisionRequestProvider:
    if value in K8S_ADDON_CONFIG_REVISION_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_ADDON_CONFIG_REVISION_REQUEST_PROVIDER_VALUES!r}"
    )
