from typing import Literal

PatchedArtifactRepositoryRequestKind = Literal["docker", "helm", "oci", "polycrate", "source"]

PATCHED_ARTIFACT_REPOSITORY_REQUEST_KIND_VALUES: set[PatchedArtifactRepositoryRequestKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_patched_artifact_repository_request_kind(value: str) -> PatchedArtifactRepositoryRequestKind:
    if value in PATCHED_ARTIFACT_REPOSITORY_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ARTIFACT_REPOSITORY_REQUEST_KIND_VALUES!r}")
