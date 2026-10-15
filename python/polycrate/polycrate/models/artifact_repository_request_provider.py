from typing import Literal

ArtifactRepositoryRequestProvider = Literal[
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

ARTIFACT_REPOSITORY_REQUEST_PROVIDER_VALUES: set[ArtifactRepositoryRequestProvider] = {
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


def check_artifact_repository_request_provider(value: str) -> ArtifactRepositoryRequestProvider:
    if value in ARTIFACT_REPOSITORY_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_REQUEST_PROVIDER_VALUES!r}")
