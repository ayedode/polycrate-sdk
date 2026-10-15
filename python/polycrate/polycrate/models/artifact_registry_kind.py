from typing import Literal

ArtifactRegistryKind = Literal["harbor"]

ARTIFACT_REGISTRY_KIND_VALUES: set[ArtifactRegistryKind] = {
    "harbor",
}


def check_artifact_registry_kind(value: str) -> ArtifactRegistryKind:
    if value in ARTIFACT_REGISTRY_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_KIND_VALUES!r}")
