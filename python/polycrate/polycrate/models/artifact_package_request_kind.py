from typing import Literal

ArtifactPackageRequestKind = Literal["docker", "helm", "oci", "polycrate", "source"]

ARTIFACT_PACKAGE_REQUEST_KIND_VALUES: set[ArtifactPackageRequestKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_artifact_package_request_kind(value: str) -> ArtifactPackageRequestKind:
    if value in ARTIFACT_PACKAGE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_REQUEST_KIND_VALUES!r}")
