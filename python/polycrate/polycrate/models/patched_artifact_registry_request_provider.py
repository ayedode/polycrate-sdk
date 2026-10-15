from typing import Literal

PatchedArtifactRegistryRequestProvider = Literal[
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

PATCHED_ARTIFACT_REGISTRY_REQUEST_PROVIDER_VALUES: set[PatchedArtifactRegistryRequestProvider] = {
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


def check_patched_artifact_registry_request_provider(value: str) -> PatchedArtifactRegistryRequestProvider:
    if value in PATCHED_ARTIFACT_REGISTRY_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ARTIFACT_REGISTRY_REQUEST_PROVIDER_VALUES!r}"
    )
