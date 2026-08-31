from typing import Literal

ArtifactKindEnum = Literal["docker", "helm", "oci", "polycrate", "source"]

ARTIFACT_KIND_ENUM_VALUES: set[ArtifactKindEnum] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_artifact_kind_enum(value: str) -> ArtifactKindEnum:
    if value in ARTIFACT_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_KIND_ENUM_VALUES!r}")
