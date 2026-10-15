from typing import Literal

ArtifactPackageKind = Literal["docker", "helm", "oci", "polycrate", "source"]

ARTIFACT_PACKAGE_KIND_VALUES: set[ArtifactPackageKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_artifact_package_kind(value: str) -> ArtifactPackageKind:
    if value in ARTIFACT_PACKAGE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_KIND_VALUES!r}")
