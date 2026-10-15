from typing import Literal

ArtifactRegistryRequestProvider = Literal[
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

ARTIFACT_REGISTRY_REQUEST_PROVIDER_VALUES: set[ArtifactRegistryRequestProvider] = {
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


def check_artifact_registry_request_provider(value: str) -> ArtifactRegistryRequestProvider:
    if value in ARTIFACT_REGISTRY_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_REQUEST_PROVIDER_VALUES!r}")
