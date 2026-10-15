from typing import Literal

PatchedK8SAddonConfigRevisionRequestProvider = Literal[
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

PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_PROVIDER_VALUES: set[PatchedK8SAddonConfigRevisionRequestProvider] = {
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


def check_patched_k8s_addon_config_revision_request_provider(
    value: str,
) -> PatchedK8SAddonConfigRevisionRequestProvider:
    if value in PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_PROVIDER_VALUES!r}"
    )
