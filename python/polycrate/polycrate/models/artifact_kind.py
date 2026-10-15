from typing import Literal

ArtifactKind = Literal["docker", "helm", "oci", "polycrate", "source"]

ARTIFACT_KIND_VALUES: set[ArtifactKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_artifact_kind(value: str) -> ArtifactKind:
    if value in ARTIFACT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_KIND_VALUES!r}")
