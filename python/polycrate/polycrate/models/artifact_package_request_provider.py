from typing import Literal

ArtifactPackageRequestProvider = Literal[
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

ARTIFACT_PACKAGE_REQUEST_PROVIDER_VALUES: set[ArtifactPackageRequestProvider] = {
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


def check_artifact_package_request_provider(value: str) -> ArtifactPackageRequestProvider:
    if value in ARTIFACT_PACKAGE_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_REQUEST_PROVIDER_VALUES!r}")
