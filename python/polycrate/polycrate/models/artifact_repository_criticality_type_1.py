from typing import Literal

ArtifactRepositoryCriticalityType1 = Literal["", "high", "low", "medium"]

ARTIFACT_REPOSITORY_CRITICALITY_TYPE_1_VALUES: set[ArtifactRepositoryCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_artifact_repository_criticality_type_1(value: str) -> ArtifactRepositoryCriticalityType1:
    if value in ARTIFACT_REPOSITORY_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_CRITICALITY_TYPE_1_VALUES!r}")
