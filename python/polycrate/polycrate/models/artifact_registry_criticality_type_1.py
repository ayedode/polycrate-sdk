from typing import Literal

ArtifactRegistryCriticalityType1 = Literal["", "high", "low", "medium"]

ARTIFACT_REGISTRY_CRITICALITY_TYPE_1_VALUES: set[ArtifactRegistryCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_artifact_registry_criticality_type_1(value: str) -> ArtifactRegistryCriticalityType1:
    if value in ARTIFACT_REGISTRY_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_CRITICALITY_TYPE_1_VALUES!r}")
