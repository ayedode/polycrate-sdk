from typing import Literal

ArtifactRegistryScope = Literal["system", "user"]

ARTIFACT_REGISTRY_SCOPE_VALUES: set[ArtifactRegistryScope] = {
    "system",
    "user",
}


def check_artifact_registry_scope(value: str) -> ArtifactRegistryScope:
    if value in ARTIFACT_REGISTRY_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_SCOPE_VALUES!r}")
