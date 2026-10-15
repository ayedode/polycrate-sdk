from typing import Literal

ArtifactRepositoryKind = Literal["docker", "helm", "oci", "polycrate", "source"]

ARTIFACT_REPOSITORY_KIND_VALUES: set[ArtifactRepositoryKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_artifact_repository_kind(value: str) -> ArtifactRepositoryKind:
    if value in ARTIFACT_REPOSITORY_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_KIND_VALUES!r}")
