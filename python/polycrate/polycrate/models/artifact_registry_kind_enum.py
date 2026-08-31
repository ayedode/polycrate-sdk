from typing import Literal

ArtifactRegistryKindEnum = Literal["harbor"]

ARTIFACT_REGISTRY_KIND_ENUM_VALUES: set[ArtifactRegistryKindEnum] = {
    "harbor",
}


def check_artifact_registry_kind_enum(value: str) -> ArtifactRegistryKindEnum:
    if value in ARTIFACT_REGISTRY_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_KIND_ENUM_VALUES!r}")
