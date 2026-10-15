from typing import Literal

ArtifactRepositoryRequestKind = Literal["docker", "helm", "oci", "polycrate", "source"]

ARTIFACT_REPOSITORY_REQUEST_KIND_VALUES: set[ArtifactRepositoryRequestKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_artifact_repository_request_kind(value: str) -> ArtifactRepositoryRequestKind:
    if value in ARTIFACT_REPOSITORY_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_REQUEST_KIND_VALUES!r}")
