from typing import Literal

PatchedArtifactPackageRequestKind = Literal["docker", "helm", "oci", "polycrate", "source"]

PATCHED_ARTIFACT_PACKAGE_REQUEST_KIND_VALUES: set[PatchedArtifactPackageRequestKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_patched_artifact_package_request_kind(value: str) -> PatchedArtifactPackageRequestKind:
    if value in PATCHED_ARTIFACT_PACKAGE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ARTIFACT_PACKAGE_REQUEST_KIND_VALUES!r}")
